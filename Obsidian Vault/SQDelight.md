---
title: SQLDelight
tags: [kmp, banco de dados, persistência]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Biblioteca KMP que gera APIs fortemente tipadas a partir de arquivos `.sq` (SQL) e oferece runtime multiplataforma (Android/iOS/JVM/Native).

## Para que serve
- Definir um esquema único e consultas SQL versionadas, e usá-los de forma segura em todos os alvos (Shared).
- Evitar erros de consulta em runtime: quebra na geração/compilação se a query estiver inválida.

## Quando usar
- Apps com cache local/offline‑first, filtros/ordenação/busca no cliente e necessidade de consistência entre Android e iOS.
- Projetos KMP que precisam de persistência relacional com um único schema compartilhado.

## Comparação
- Room: Android‑only; não atende Shared.
- CoreData: iOS‑only; duplicaria regras/esquemas.
- Realm Kotlin: KMP, mas formato próprio (não SQL) e menos transparência para queries complexas.
