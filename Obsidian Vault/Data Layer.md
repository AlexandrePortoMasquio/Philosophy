---
title: Camada de Dados (Data)
tags: [arquitetura, kmp, dados]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Camada responsável por obter e persistir informações (rede, banco, cache), expondo-as ao domínio por meio de contratos (repositórios) estáveis.

## No KMP
- Repositórios implementam interfaces do domínio e orquestram fontes: remota (Ktor) e local (SQLDelight), aplicando políticas (offline‑first, TTL, reconciliação).
- Sem dependências específicas de plataforma no shared; engines/drivers entram por source sets/bordas.

## Padrões
- [[DTO]]: modela payload externo; nunca expor diretamente à UI.
- Repository: contrato no domínio, implementação em data; mapeia DTO/DbRow → Domain.
- Mapper: funções puras para conversão; cobertas por testes.
- Estratégias: backoff/timeout/circuit breaker em chamadas remotas quando necessário.

## Boas práticas
- Erros: converter exceções em `DomainError` antes de sair da camada de dados.
- Consistência: idempotência em upserts; reconciliação por chave primária.
- Observabilidade: logs nos pontos de orquestração (requisições, cache miss/hit, erros).

## Ligações
- [[Ktor]] · [[SQLDelight]] · [[TTL]] · [[KMP]]
