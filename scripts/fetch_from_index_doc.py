#!/usr/bin/env python3
import argparse
import os
import re
import sys
from typing import Dict, List, Optional, Tuple

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Escopos necessários para ler o índice (Docs) e baixar capítulos (Drive)
SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/documents.readonly",
]


def slugify(text: str) -> str:
    import unicodedata

    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\-\s_]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-") or "sem-titulo"


def extract_file_id(url: str) -> Optional[str]:
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


def parse_index_links(docs_service, index_doc_id: str) -> List[Tuple[str, str]]:
    """Retorna lista [(url, texto_link)] do documento índice."""
    doc = docs_service.documents().get(documentId=index_doc_id).execute()
    out: List[Tuple[str, str]] = []
    for block in doc.get("body", {}).get("content", []):
        para = block.get("paragraph")
        if not para:
            continue
        for el in para.get("elements", []):
            tr = el.get("textRun")
            if not tr:
                continue
            style = tr.get("textStyle", {})
            link = style.get("link") or {}
            url = link.get("url")
            if not url:
                continue
            text = (tr.get("content") or "").strip()
            if not text:
                text = url
            out.append((url, text))
    return out


def mime_for_ext(ext: str) -> str:
    mapping = {
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "txt": "text/plain",
        "md": "text/plain",
        "html": "text/html",
    }
    return mapping.get(ext, "text/plain")


def export_gdoc(drive_service, file_id: str, mime_type: str) -> bytes:
    request = drive_service.files().export(fileId=file_id, mimeType=mime_type)
    return request.execute()


def drive_title(drive_service, file_id: str) -> Optional[str]:
    try:
        meta = drive_service.files().get(fileId=file_id, fields="name").execute()
        return meta.get("name")
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Lê um índice no Google Docs e baixa os capítulos linkados, sem alterar o conteúdo.")
    parser.add_argument("--index-doc", required=True, help="URL ou ID do Google Doc que contém o índice")
    parser.add_argument("--out", default="livro", help="Pasta de saída")
    parser.add_argument("--ext", default="docx", choices=["docx", "txt", "md", "html"], help="Extensão dos arquivos")
    parser.add_argument("--naming", default="title", choices=["title"], help="Nome por título (única opção)")
    parser.add_argument("--prefix", action="store_true", help="Prefixar arquivos com numeração 01-, 02-, ...")
    parser.add_argument("--console", action="store_true", help="Usar fluxo OAuth em modo console (cola o código)")
    parser.add_argument("--report", default=None, help="Caminho do CSV para registrar negados/erros (padrão: livro/erros_permissao.csv). Use '' para desativar.")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescrever arquivos existentes (por padrão, o script pula arquivos já presentes)")

    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    # Extrai ID do índice
    index_id = args.index_doc
    if "/" in index_id or "google" in index_id:
        maybe = extract_file_id(index_id)
        if not maybe:
            sys.exit("Não consegui extrair o ID do documento de índice a partir do link.")
        index_id = maybe

    creds = get_credentials(use_console=args.console)
    docs = build("docs", "v1", credentials=creds)
    drive = build("drive", "v3", credentials=creds)

    links = parse_index_links(docs, index_id)
    if not links:
        sys.exit("Nenhum link encontrado no índice. Verifique o documento.")

    # Dedupe por file_id, preservando ordem
    ordered: Dict[str, Dict[str, str]] = {}
    for url, text in links:
        fid = extract_file_id(url)
        if not fid:
            continue
        if fid not in ordered:
            ordered[fid] = {"url": url, "text": text}

    if not ordered:
        sys.exit("O índice não contém links para Google Docs válidos.")

    fids = list(ordered.keys())
    pad = max(2, len(str(len(fids))))

    negados_rows = []
    outras_rows = []

    for i, fid in enumerate(fids, 1):
        idx_prefix = f"{i:0{pad}d}-" if args.prefix else ""
        idx_info = ordered[fid]

        title_from_drive = drive_title(drive, fid) or ""
        title_candidate = (title_from_drive or idx_info.get("text") or fid).strip()
        name_part = slugify(title_candidate)
        out_path = os.path.join(args.out, f"{idx_prefix}{name_part}.{args.ext}")

        # Se o arquivo já existe e não queremos sobrescrever, pule antes de baixar
        if os.path.exists(out_path) and not args.overwrite:
            print(f"[skip] Já existe: {out_path}")
            continue

        try:
            mime = mime_for_ext(args.ext)
            content = export_gdoc(drive, fid, mime)
        except HttpError as e:
            status = getattr(e, "resp", None).status if getattr(e, "resp", None) else None
            url = idx_info.get("url", "")
            if status in (403, 404):
                negados_rows.append({
                    "tipo": "negado",
                    "status": status or "",
                    "file_id": fid,
                    "nome": title_candidate,
                    "url": url,
                    "erro": str(e).replace("\n", " ")[:1000],
                })
                print(f"[negado {status}] {title_candidate} ({fid}) — {url}")
            else:
                outras_rows.append({
                    "tipo": "erro",
                    "status": status or "",
                    "file_id": fid,
                    "nome": title_candidate,
                    "url": url,
                    "erro": str(e).replace("\n", " ")[:1000],
                })
                print(f"[erro {status}] Falha ao exportar {title_candidate}: {e}")
            continue
        except Exception as e:
            url = idx_info.get("url", "")
            outras_rows.append({
                "tipo": "erro",
                "status": "",
                "file_id": fid,
                "nome": title_candidate,
                "url": url,
                "erro": str(e).replace("\n", " ")[:1000],
            })
            print(f"[erro] Falha ao exportar {title_candidate}: {e}")
            continue

        # Escreve exatamente os bytes exportados, sem cabeçalho
        with open(out_path, "wb") as f:
            f.write(content)
        print(f"[ok] Salvo: {out_path}")

    # Escreve relatório, se houver negados/erros
    if (negados_rows or outras_rows) and (args.report is None or args.report != ""):
        import csv
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
