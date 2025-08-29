---
title: API
tags: [engenharia de software, api, integração]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Contrato de integração entre sistemas: define recursos, operações, formatos, erros e garantias (latência, limites, segurança).

## Estilos
- REST: recursos sobre [[HTTP]] com verbos, status, cache; simples e amplamente suportado.
- GraphQL: consulta declarativa (um endpoint), evita over/underfetch; exige governança de schema e caching específico.
- gRPC: contratos binários (Protocol Buffers), eficiente e tipado; forte em chamadas serviço-serviço.

## Boas Práticas
- Versionamento e compatibilidade progressiva; deprecar com prazos e métricas de uso.
- Idempotência para operações de escrita (chaves idempotentes, safe retries).
- Modelo de erros consistente (códigos + detalhes), mapeável para [[Domain|erros de domínio]].
- Paginação, filtragem e ordenação previsíveis; limites de taxa e cota.
- Segurança: autenticação, autorização baseada em escopos, proteção contra abuso.

## Ligações
- [[Backend]], [[Banco de Dados]], [[Sistemas Distribuídos/Sistemas Distribuídos|Sistemas Distribuídos]], [[HTTP]], [[Domain]].

