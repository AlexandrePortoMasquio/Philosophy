---
title: ViewModel
tags: [android, mvvm]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Componente de apresentação que mantém estado de UI e coordena ações da tela, sobrevivendo a recriações.

## Boas práticas
- Expor `StateFlow<UiState>` e intents; nenhuma referência a APIs de View/Activity.
- Delegar regras a use cases; injetar dependências por construtor (DI).

## Ligações
- [[Arquitetura MVVM]] · [[Arquitetura Android]]
