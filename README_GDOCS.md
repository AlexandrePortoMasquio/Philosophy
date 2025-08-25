Guia rápido: importar capítulos do Google Docs

1) Crie credenciais no Google Cloud
- Acesse: https://console.cloud.google.com/apis/credentials
- Crie um projeto (se ainda não tiver).
- Habilite as APIs: "Google Drive API" (e opcionalmente "Google Docs API").
- Em "Credenciais" > "Criar credenciais" > "ID do cliente OAuth".
- Tipo: Aplicativo para computador. Baixe o JSON e salve na raiz deste projeto como `credentials.json`.

2) Prepare o índice
- Edite `indice.csv` e liste: `slug,title,url` para cada capítulo.
- O `url` pode ser o link do Google Docs (não precisa ser público).

3) Instale dependências (opcional em venv)
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4) Opção A: usar o índice (Google Docs)
Se você tem um documento-índice com os links para cada capítulo, rode:
```
python scripts/fetch_from_index_doc.py --index-doc "https://docs.google.com/document/d/SEU_INDICE_ID/edit" --out livro --ext docx --prefix
```
- `--prefix` numera os arquivos como `01-...`, `02-...` (opcional).
- Por padrão o nome é baseado no título do documento do Drive. O conteúdo é gravado exatamente como exportado (sem cabeçalhos ou alterações).
 - Quando houver documentos sem permissão (403/404), o script registra um relatório CSV em `livro/erros_permissao.csv` com o ID, link e nome.
 - Padrão: arquivos existentes NÃO são sobrescritos (`[skip]`). Para forçar regravação, use `--overwrite`.
 - Sempre é gerado `livro/bloqueados.txt` com um nome por linha dos documentos sem acesso (sobrescreve a cada execução; vazio se nenhum).

4b) Opção B: usar CSV (manual)
Se preferir listar manualmente os capítulos num CSV:
```
python scripts/fetch_gdocs.py --index indice.csv --out livro --ext docx --naming slug
```
- Na primeira execução abrirá uma janela de autorização Google. Aceite com a sua conta que tem acesso aos Docs.
- Os arquivos serão salvos na pasta `livro/` como `.docx` (conteúdo exportado puro, sem cabeçalho adicional).
 - Em caso de erro de permissão, um relatório é gravado em `livro/erros_permissao.csv`.
 - Padrão: arquivos existentes NÃO são sobrescritos (`[skip]`). Para forçar regravação, use `--overwrite`.
 - Também é gerado `livro/bloqueados.txt` com os nomes dos documentos sem acesso (sobrescrito sempre).

Dicas
- DOCX preserva formatação; texto puro (`--ext txt`) perde estilos.
- Se preferir `.txt`, use `--ext txt`.
- Também é possível `--ext html` para exportar como HTML.
- Se quiser nomear pelos títulos ao invés do slug, use `--naming title`.
- Caso veja erro de permissão, confirme que a conta autorizada tem acesso aos documentos.
