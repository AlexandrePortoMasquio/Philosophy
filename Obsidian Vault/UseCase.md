---
title: Use Case (Aplicação)
tags: [aplicação, ports, kmp]
created: 2025-08-31
updated: 2025-08-31
---

## Ideia
- Caso de uso é um serviço de aplicação que expõe uma intenção do sistema (o “o quê”), orquestrando portas de saída (repositórios/gateways) sem conhecer UI ou infraestrutura.
- Em KMP, define‑se como interface no [[Domain|domínio]] (driving port); a implementação depende apenas de [[Port|portas]] e tipos puros (p.ex., `AppResult`).

## Diretrizes
- Foco: uma intenção clara (p.ex., “obter lista”, “buscar detalhe”).
- Sem estado interno e sem thread policy (o chamador decide contexto/dispatcher).
- Sem dependência de UI/frameworks; entrada/saída por valores.
- Sem acoplamento entre casos de uso: não chamar outro use case diretamente.

## Evitando recursividade/composição cíclica
- DI acíclica: cada caso de uso recebe apenas portas de saída (repositório, clock, etc.); não recebe outros casos de uso como dependência.
- Composição no nível superior: [[ViewModel]]/[[Facade]] agregam chamadas a múltiplos casos de uso, preservando a independência entre eles.
- Orquestradores dedicados (quando necessário): criar um “application service/coordinator” específico que coordene múltiplas operações, ainda dependendo só de portas — nunca de use cases entre si.
- Regras de módulo: o [[Domain]] não exporta fábricas que conectem um caso de uso a outro; [[Adapter]]/DI só ligam use cases → portas.
- Testes: testes de use case usam fakes de portas; inexistência de mocks de outros use cases detecta acoplamento indevido.

## Assinatura típica (Kotlin)
- Função única `invoke(params): AppResult<Out>` (ou `suspend`), com tipos de entrada/saída no domínio.

## Ligações
- [[Domain]] · [[Port]] · [[Adapter]] · [[Facade]] · [[ViewModel]] · [[Ciência da Computação/Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]]

