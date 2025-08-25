#!/usr/bin/env python3
import argparse
import os
import re
import shutil
from typing import List


def slugify(text: str) -> str:
    import unicodedata

    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\-\s_]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-") or "sem-titulo"


def list_files(src: str, exts: List[str]) -> List[str]:
    all_files: List[str] = []
    for entry in os.scandir(src):
        if not entry.is_file():
            continue
        name = entry.name
        if "." in name:
            ext = name.rsplit(".", 1)[1].lower()
        else:
            ext = ""
        if exts and ext not in exts:
            continue
        all_files.append(entry.path)
    return sorted(all_files, key=lambda p: os.path.basename(p).lower())


def main():
    parser = argparse.ArgumentParser(description="Organiza capítulos já exportados manualmente, copiando para a pasta de livro sem alterar o conteúdo.")
    parser.add_argument("--src", default="originais", help="Pasta de origem com os arquivos exportados (ex.: .docx)")
    parser.add_argument("--out", default="livro", help="Pasta de destino onde ficarão os capítulos")
    parser.add_argument("--ext", default="docx", help="Extensões a considerar, separadas por vírgula (ex.: docx,txt). Padrão: docx")
    parser.add_argument("--prefix", action="store_true", help="Prefixar arquivos com numeração 01-, 02-, ...")
    parser.add_argument("--keep-name", action="store_true", help="Manter o nome original do arquivo (sem slugify)")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescrever arquivos existentes (padrão: pular existentes)")
    parser.add_argument("--report", default=None, help="CSV de mapeamento (origem→destino). Padrão: <out>/mapeamento.csv")
    parser.add_argument("--dry-run", action="store_true", help="Apenas mostrar o que seria feito, sem copiar")

    args = parser.parse_args()

    exts = [e.strip().lower() for e in args.ext.split(",") if e.strip()]

    if not os.path.isdir(args.src):
        raise SystemExit(f"Pasta de origem não encontrada: {args.src}")

    os.makedirs(args.out, exist_ok=True)

    files = list_files(args.src, exts)
    if not files:
        print("Nenhum arquivo encontrado na origem com as extensões informadas.")
        return

    pad = max(2, len(str(len(files)))) if args.prefix else 0

    used_names = set()
    rows = []

    for i, src_path in enumerate(files, 1):
        base = os.path.basename(src_path)
        stem = base.rsplit(".", 1)[0]
        ext = base.rsplit(".", 1)[1].lower() if "." in base else ""

        name_part = stem if args.keep-name else slugify(stem)
        prefix = f"{i:0{pad}d}-" if args.prefix else ""
        candidate = f"{prefix}{name_part}.{ext}"

        # Evita colisões gerando sufixos -2, -3, ...
        final_name = candidate
        counter = 2
        while final_name in used_names:
            suffix = f"-{counter}"
            final_name = f"{prefix}{name_part}{suffix}.{ext}"
            counter += 1
        used_names.add(final_name)

        dest_path = os.path.join(args.out, final_name)

        action = "skip"
        if os.path.exists(dest_path) and not args.overwrite:
            print(f"[skip] Já existe: {dest_path}")
        else:
            action = "copy"
            print(f"[copy] {src_path} -> {dest_path}")
            if not args.dry_run:
                shutil.copy2(src_path, dest_path)

        rows.append({
            "origem": src_path,
            "destino": dest_path,
            "acao": action,
        })

    # Escreve mapeamento
    try:
        import csv
        report_path = args.report or os.path.join(args.out, "mapeamento.csv")
        with open(report_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["origem", "destino", "acao"])
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
        print(f"[relatório] Mapeamento salvo em: {report_path}")
    except Exception as e:
        print(f"[aviso] Não foi possível escrever o relatório de mapeamento: {e}")


if __name__ == "__main__":
    main()

