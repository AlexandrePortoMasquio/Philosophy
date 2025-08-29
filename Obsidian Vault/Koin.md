---
title: Koin
tags: [kmp, di]
created: 2025-08-29
updated: 2025-08-29
---
[Injeção de Dependência](Injeção%20de%20Dependência.md) 
## Por que usar no KMP
- Multiplataforma: funciona no Shared sem dependências de plataforma; ideal para orquestrar wiring no app e manter domínio/dados com injeção por construtor.
- Simples: DSL clara; sem codegen, o que reduz atrito e tempo de build em um desafio técnico.
- Alternativas: Kodein (KMP); Dagger/Hilt (Android‑only) — mantemos Koin para Shared e Koin Android só na apresentação.
## Koin é a melhor escolha no KMP?
- É uma escolha pragmática: funciona no Shared, é simples e evita [[codegen]]; ótima para projeto de referência/desafio técnico.
- Mantemos DIP com injeção por construtor e contratos no domínio/dados; o contêiner (Koin) fica nas bordas.
- Alternativas: Kodein (KMP) também é viável; Hilt/Dagger são Android‑only e ficam fora do Shared.


## Padrão recomendado
- Shared: preferir construtor + interfaces; Koin para modules de domínio/dados apenas como wiring.
- Android: Koin Android + koin‑androidx‑compose para ViewModel e escopos de tela.
- iOS: composition root em Swift; opcional iniciar Koin do Shared.
