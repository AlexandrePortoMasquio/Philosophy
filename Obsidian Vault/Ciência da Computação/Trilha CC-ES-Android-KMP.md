---
title: Trilha CC → ES → Android/KMP
tags: [trilha, arquitetura, ciência da computação, mobile]
created: 2025-08-28
updated: 2025-08-28
---

## Objetivo
- Conectar princípios de [[Ciência da Computação]] a decisões de [[Engenharia de Software]] e especificidades de [[Engenharia de Software/Engenharia de Software Mobile/Arquitetura Android|Arquitetura Android]] e [[Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]].

## Critérios Norteadores (Filosofia → Prática)
- [[Critérios Naturais]] (simplicidade/robustez), [[Granularidade]] (limites), [[Identidade]] (contratos), [[Controle]] (efeitos, observabilidade), [[Lei da Variedade Requisitada]].

## Passos
1. Modelar domínio (formas, invariantes) → escolher estruturas e algoritmos.
2. Definir limites (módulos, camadas) → arquitetura de software.
3. Especializar para Android: fluxo UDF, DI, persistência, offline‑first, testes.
4. Avaliar compartilhamento via KMP: o que vai para o shared (domínio/dados), o que fica nativo (UI/integrações).
5. Medir e evoluir: métricas de desempenho, estabilidade, complexidade de mudanças.

## Artefatos
- ADRs com contexto/alternativas/decisões; diagramas; contratos de API; guias de testes.

## Ligações
- [[Informação]] · [[Computação]] · [[Engenharia de Software/Arquitetura de Software|Arquitetura de Software]] · [[Engenharia de Software/Engenharia de Software Mobile/KMP|KMP]]
