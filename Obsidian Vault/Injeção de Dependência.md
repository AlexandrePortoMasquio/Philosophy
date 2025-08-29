---
title: Injeção de Dependência
tags: [di]
created: 2025-08-29
updated: 2025-08-29
---

## Koin é a melhor escolha no KMP?
- É uma escolha pragmática: funciona no Shared, é simples e evita codegen; ótima para projeto de referência/desafio técnico.
- Mantemos DIP com injeção por construtor e contratos no domínio/dados; o contêiner (Koin) fica nas bordas.
- Alternativas: Kodein (KMP) também é viável; Hilt/Dagger são Android‑only e ficam fora do Shared.
