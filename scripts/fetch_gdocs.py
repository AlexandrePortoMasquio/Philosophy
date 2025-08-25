#!/usr/bin/env python3
import argparse
import csv
import os
import re
import sys
from typing import Optional

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\-\s_]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-") or "sem-titulo"


def extract_file_id(url: str) -> Optional[str]:
    # Common GDocs patterns
    patterns = [
        r"docs\.google\.com/document/d/([a-zA-Z0-9-_]+)",
        r"drive\.google\.com/file/d/([a-zA-Z0-9-_]+)",
        r"drive\.google\.com/open\?id=([a-zA-Z0-9-_]+)",
        r"docs\.google\.com/document/u/\d+/d/([a-zA-Z0-9-_]+)",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


def get_credentials(creds_path: str = "credentials.json", token_path: str = "token.json", use_console: bool = False) -> Credentials:
    creds: Optional[Credentials] = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_path):
                sys.exit(
                    f"Arquivo {creds_path} não encontrado. Baixe as credenciais OAuth do Google Cloud e salve como {creds_path}."
                )
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            if use_console:
                creds = flow.run_console()
            else:
                creds = flow.run_local_server(port=0)
        with open(token_path, "w") as token:
            token.write(creds.to_json())
    return creds


def mime_for_ext(ext: str) -> str:
    mapping = {
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "txt": "text/plain",
        "md": "text/plain",
        "html": "text/html",
    }
    return mapping.get(ext, "text/plain")


def export_gdoc(drive, file_id: str, mime_type: str) -> bytes:
    request = drive.files().export(fileId=file_id, mimeType=mime_type)
    return request.execute()


def main():
    parser = argparse.ArgumentParser(description="Baixa capítulos do Google Docs para arquivos locais, sem alterar o conteúdo.")
    parser.add_argument("--index", default="indice.csv", help="Caminho do CSV com slug,title,url")
    parser.add_argument("--out", default="livro", help="Pasta de saída para os capítulos")
    parser.add_argument("--ext", default="docx", choices=["docx", "txt", "md", "html"], help="Extensão dos arquivos gerados")
    parser.add_argument("--console", action="store_true", help="Usar fluxo OAuth em modo console (cola o código)")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescrever arquivos existentes (por padrão, o script pula arquivos já presentes)")
    parser.add_argument("--report", default=None, help="Caminho do CSV para registrar negados/erros (padrão: livro/erros_permissao.csv). Use '' para desativar.")
    parser.add_argument(
        "--naming",
        default="slug",
        choices=["slug", "title"],
        help="Usar 'slug' ou 'title' para nome do arquivo",
    )

    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    creds = get_credentials(use_console=args.console)
    drive = build("drive", "v3", credentials=creds)

    negados_rows = []
    outras_rows = []

    with open(args.index, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"slug", "title", "url"}
        if not required.issubset(reader.fieldnames or set()):
            sys.exit(f"CSV deve conter colunas: {', '.join(sorted(required))}")
        for row in reader:
            slug = (row.get("slug") or "").strip()
            title = (row.get("title") or "").strip()
            url = (row.get("url") or "").strip()

            if not url:
                print("[pular] Linha sem URL")
                continue

            file_id = extract_file_id(url)
            if not file_id:
                print(f"[erro] Não consegui extrair ID do link: {url}")
                continue

            name_part = slug if args.naming == "slug" and slug else slugify(title or slug or file_id[:8])
            out_path = os.path.join(args.out, f"{name_part}.{args.ext}")

            # Se o arquivo já existe e não queremos sobrescrever, pule antes de baixar
            if os.path.exists(out_path) and not args.overwrite:
                print(f"[skip] Já existe: {out_path}")
                continue

            try:
                mime = mime_for_ext(args.ext)
                content = export_gdoc(drive, file_id, mime)
            except HttpError as e:
                status = getattr(e, "resp", None).status if getattr(e, "resp", None) else None
                name = (title or slug or file_id)
                if status in (403, 404):
                    negados_rows.append({
                        "tipo": "negado",
                        "status": status or "",
                        "file_id": file_id,
                        "nome": name,
                        "url": url,
                        "erro": str(e).replace("\n", " ")[:1000],
                    })
                    print(f"[negado {status}] {name} ({file_id}) — {url}")
                else:
                    outras_rows.append({
                        "tipo": "erro",
                        "status": status or "",
                        "file_id": file_id,
                        "nome": name,
                        "url": url,
                        "erro": str(e).replace("\n", " ")[:1000],
                    })
                    print(f"[erro {status}] Falha ao exportar {name}: {e}")
                continue
            except Exception as e:
                name = (title or slug or file_id)
                outras_rows.append({
                    "tipo": "erro",
                    "status": "",
                    "file_id": file_id,
                    "nome": name,
                    "url": url,
                    "erro": str(e).replace("\n", " ")[:1000],
                })
                print(f"[erro] Falha ao exportar {name}: {e}")
                continue

            # Escreve exatamente os bytes exportados, sem inserir cabeçalho ou alterações
            with open(out_path, "wb") as out:
                out.write(content)
            print(f"[ok] Salvo: {out_path}")

    # Escreve relatório, se houver negados/erros
    if (negados_rows or outras_rows) and (args.report is None or args.report != ""):
        report_path = args.report if args.report is not None else os.path.join(args.out, "erros_permissao.csv")
        fieldnames = ["tipo", "status", "file_id", "nome", "url", "erro"]
        try:
            with open(report_path, "w", newline="", encoding="utf-8") as rf:
                writer = csv.DictWriter(rf, fieldnames=fieldnames)
                writer.writeheader()
                for row in negados_rows + outras_rows:
                    writer.writerow(row)
            print(f"[relatório] {len(negados_rows)} negados, {len(outras_rows)} outros erros → {report_path}")
        except Exception as e:
            print(f"[aviso] Não foi possível escrever o relatório: {e}")

    # Sempre escreva a lista de bloqueados (um nome por linha), sobrescrevendo a cada execução
    try:
        blocked_path = os.path.join(args.out, "bloqueados.txt")
        with open(blocked_path, "w", encoding="utf-8") as bf:
            for row in negados_rows:
                name = (row.get("nome") or "").strip() or row.get("file_id") or ""
                bf.write(f"{name}\n")
        print(f"[bloqueados] {len(negados_rows)} itens → {blocked_path}")
    except Exception as e:
        print(f"[aviso] Não foi possível escrever bloqueados.txt: {e}")


if __name__ == "__main__":
    main()
