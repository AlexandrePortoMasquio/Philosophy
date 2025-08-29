---
title: Backend
tags: [engenharia de software, backend, serviços]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Camada servidor que expõe [[API]]s, aplica regras de negócio, integra sistemas externos e persiste estado em [[Banco de Dados]].
- Foca em confiabilidade, segurança, escalabilidade e manutenibilidade sob restrições de custo e tempo.

## Responsabilidades
- Modelagem de domínio e casos de uso (aplicação do core); validação e invariantes.
- Persistência e consulta eficientes; indexação e consistência.
- Integrações (pagamentos, mensageria, terceiros) com resiliência (retries/backoff, circuit breaker).
- Segurança: autenticação, autorização, rate limiting, auditoria.
- Observabilidade: logs estruturados, métricas, traços, orçamentos de erro.

## Estilos Arquiteturais
- Monólito modular vs. microsserviços vs. serverless; síncrono (HTTP/gRPC) vs. assíncrono (eventos/mensageria).
- Idempotência e deduplicação como padrões para robustez em reentregas.

## Ligações
- [[API]], [[Banco de Dados]], [[Arquitetura de Software]], [[Sistemas Distribuídos/Sistemas Distribuídos|Sistemas Distribuídos]], [[Princípios SOLID]], [[Domain]].

## Notas
- Contratos estáveis e evolutivos: separar o modelo do domínio do modelo exposto em APIs; usar versionamento e compatibilidade progressiva.

