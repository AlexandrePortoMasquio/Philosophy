---
title: SQLDelight
tags: [kmp, banco de dados, persistência]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Biblioteca KMP que gera APIs fortemente tipadas a partir de arquivos `.sq` (SQL) e oferece runtime multiplataforma (Android/iOS/JVM/Native).

## Por que usar no KMP
- Um único schema e consultas no Shared (commonMain); drivers específicos (Android/Native) só nas bordas.
- Segurança de compilação: queries inválidas falham no build (não em runtime).
- Expressividade/Desempenho: filtros/ordenação no SQL; ideal para offline‑first.

## Quando usar
- Cache local para lista/detalhe/busca; necessidade de consistência entre Android e iOS.

## Comparação
- Room: Android‑only; não atende Shared.
- CoreData: iOS‑only; duplicaria regras/esquemas.
- Realm Kotlin: KMP, mas formato próprio (não SQL) e menos transparência para queries complexas (sem schema relacional explícito; tuning/operação menos direta).

## Exemplos
```sql
-- select
selectAll:
SELECT * FROM shop ORDER BY name;

-- insert or replace
insertOrReplace:
INSERT OR REPLACE INTO shop(id, name, address, rating)
VALUES (?, ?, ?, ?);
```

## Testes (driver em memória)
```kotlin
val driver = JdbcSqliteDriver(JdbcSqliteDriver.IN_MEMORY)
CatalogDatabase.Schema.create(driver)
val db = CatalogDatabase(driver)
// execute queries and assert
```

## iOS (gotchas)
- Acesso serializado ao SQLite; evitar concorrência não controlada no driver nativo.
- Criar e fechar conexões com cuidado para não vazar recursos.

Ver também: [[KMP]].
