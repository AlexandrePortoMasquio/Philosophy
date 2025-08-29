---
title: App.kt (Composable raiz)
tags: [android, compose]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Arquivo que define o composable raiz (ex.: `RootApp`) chamado pela `MainActivity` via `setContent { ... }`.
- Responsável por tema, navegação e estado de UI.

## Relação com KMP
- No nosso KMP, a UI é específica por plataforma; o composable raiz fica em `androidMain` (Android) e a tela equivalente fica em SwiftUI (iOS).
- Inicializações globais (DI/log/SqlDriver) acontecem na classe `Application` (ex.: `MyAppApplication`), não aqui.
