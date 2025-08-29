---
title: DTO (Data Transfer Object)
tags: [arquitetura, kmp, dados]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Objeto simples para transportar dados entre camadas/limites (ex.: API ↔ app), sem lógica de negócio e frequentemente espelhando o formato externo (JSON, DB).

## No KMP
- DTOs representam payloads da rede (Ktor + kotlinx.serialization) e/ou linhas do DB (SQLDelight) — não são usados diretamente pela UI.
- Mapeamento explícito: `DTO → Domain` e `DbRow → Domain` via mappers dedicados (SRP/testabilidade).
- Interop iOS: manter campos e nullability claros para geração/bridge mais previsível.

## Diretrizes
- Evitar lógica em DTOs; manter somente dados.
- Tolerar campos opcionais/unknown (Json { ignoreUnknownKeys = true }).
- Converter datas/formatos (ex.: string → `Instant`) nos mappers, não na UI.

## Ligações
- [[Data]] · [[Ktor]] · [[SQLDelight]] · [[KMP]]
