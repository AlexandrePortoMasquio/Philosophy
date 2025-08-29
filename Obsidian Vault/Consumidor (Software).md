---
title: Consumidor de Dados
tags: [arquitetura, kmp]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Qualquer componente que consome contratos de dados (ex.: `Repository`, `UseCase`) para produzir estado/ações.

## Quem são
- No domínio (Shared/KMP): casos de uso consomem repositórios para aplicar regras de negócio.
- Android: ViewModel (MVVM/UDF) consome `UseCase`/`Repository` e expõe `UiState` para Compose.
- iOS: objetos de estado (ObservableObject/State) em SwiftUI consomem `UseCase`/adapters do shared e expõem `@Published`/`Publisher`.

## Diretrizes (KMP)
- Ports/Adapters: contratos no domínio; implementações concretas em data/features; composição via DI nas bordas.
- Erros: `DomainError` tipado; nunca propagar exceções para UI.
- Reatividade: `Flow/StateFlow` no shared; adaptação para Combine no iOS.
