TODO por que usar no [[KMP]]
## TODOs
- Adicionar exemplos de arquivo `.sq` (select, insert, join).
- Demonstrar uso com driver em memória para testes.
- Registrar gotchas em iOS (acesso serial ao SQLite).

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
