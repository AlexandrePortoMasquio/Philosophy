---
title: Koin
tags: [kmp, di]
created: 2025-08-29
updated: 2025-08-29
---

## Por que usar no KMP
- Multiplataforma: funciona no Shared sem dependências de plataforma; ideal para orquestrar wiring no app e manter domínio/dados com injeção por construtor.
- Simples: DSL clara; sem codegen, o que reduz atrito e tempo de build em um desafio técnico.
- Alternativas: Kodein (KMP); Dagger/Hilt (Android‑only) — mantemos Koin para Shared e Koin Android só na apresentação.

## Padrão recomendado
- Shared: preferir construtor + interfaces; Koin para modules de domínio/dados apenas como wiring.
- Android: Koin Android + koin‑androidx‑compose para ViewModel e escopos de tela.
- iOS: composition root em Swift; opcional iniciar Koin do Shared.
