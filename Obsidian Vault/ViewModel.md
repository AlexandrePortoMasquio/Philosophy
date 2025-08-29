---
title: ViewModel
tags: [android, mvvm]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Componente de apresentação que mantém estado de UI e coordena ações da tela, sobrevivendo a recriações.

## Diferenças (Controller vs Presenter)
- Controller (MVC): recebe input e coordena View/Model; em apps móveis costuma acumular responsabilidades e referências à View.
- Presenter (MVP): empurra atualizações para a View via interface; exige boilerplate de contrato e ainda segura referência à View.
- ViewModel (MVVM): expõe estado reativo (StateFlow/LiveData) e a View observa; não referencia a View, é lifecycle‑aware e mais testável.

## Boas práticas
- Expor `StateFlow<UiState>` e intents; nenhuma referência a APIs de View/Activity.
- Delegar regras a use cases; injetar dependências por construtor (DI).

## Ligações
- [[Arquitetura MVVM]] · [[Arquitetura Android]] · [[KMP]]
