---
title: HTTP
tags: [redes, http]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Protocolo de aplicação para troca de recursos (requisições/respostas) com métodos (GET/POST/PUT/DELETE), cabeçalhos, status codes (2xx/4xx/5xx) e corpo (geralmente JSON).

## No KMP (com [[Ktor]])
- Cliente HTTP multiplataforma no shared (`ktor-client-core`), com engines por plataforma (OkHttp/Darwin).
- ContentNegotiation + `kotlinx.serialization` para JSON; `ignoreUnknownKeys=true` para robustez a campos extras.
- Timeouts e backoff configuráveis; erros mapeados para `DomainError` (Timeout/Network/etc.).

## Boas práticas
- Definir base URL e endpoints centralizados.
- Tratar status não‑2xx como falha de domínio (sem vazar exceções). 
- Logar requests/respostas em debug, anonimizar dados sensíveis.
