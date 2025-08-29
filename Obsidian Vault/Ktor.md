---
title: Ktor Client
tags: [kmp, http]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Cliente HTTP multiplataforma do ecossistema Kotlin; extensível por plugins (content negotiation, logging, timeouts).

## Por que usar no KMP
- Código de rede em `commonMain`; engines entram por source sets (OkHttp no Android, Darwin no iOS).
- Integração direta com `kotlinx.serialization` para JSON.

TODO Se o ktor já serializa o json, ainda é necessário usar SQDelight? Por quê? É porque o ktor substitui o [[Retrofit]], enquanto o SQDelight substitui o [[Room]]?

## Padrão no projeto
- Shared: `HttpClient { install(ContentNegotiation) { json(Json { ignoreUnknownKeys = true }) } }`.
- Android: `io.ktor:ktor-client-okhttp`; iOS: `io.ktor:ktor-client-darwin`.
- Erros e timeouts padronizados; backoff para falhas transitórias.

## Ligações
- [[KMP]] · [[SQLDelight]] (cache offline‑first)
