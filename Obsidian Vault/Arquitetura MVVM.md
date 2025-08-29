---
title: Arquitetura MVVM
tags: [android, arquitetura]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Separar UI (View), lógica de apresentação (ViewModel) e modelo (Domain/Data) para facilitar teste e evolução.

## Em Android (Compose)
- ViewModel expõe `StateFlow<UiState>` e recebe intents; reducer atualiza estado imutável.
- Evitar lógica de domínio na View; delegar a use cases e repositórios.

## Ligações
- [[View Model]] · [[Arquitetura Android]] · [[KMP]]
