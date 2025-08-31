---
title: Compose Multiplatform
tags: [compose, ui, kmp]
created: 2025-08-31
updated: 2025-08-31
---

## Ideia
- Toolkit declarativo da JetBrains para interfaces com [[Kotlin]], originado do Jetpack Compose e estendido a múltiplas plataformas (Android, Desktop, Web e, em progresso, iOS via Skiko/Skia).
- No contexto de [[KMP]], permite compartilhar UI em certas plataformas e/ou compartilhar apenas domínio/dados, mantendo UI nativa quando preferido.

## Por que usar (no projeto)
- Produtividade: mesma mentalidade declarativa (estado → UI) em Android e Desktop; interoperável com código KMP.
- Integração: consome diretamente fluxos/estados do shared (ViewModels/UseCases) sem adapters pesados.
- Flexibilidade: adotamos UI nativa no iOS ([[SwiftUI]]) para atender requisitos e demonstrar domínio nativo; no Android, usamos Compose para velocidade e consistência.

## Integração com [[KMP]]
- Camada shared expõe casos de uso e repositórios; a UI Compose (Android) observa estados (Loading/Empty/Error/Content) e renderiza.
- Bibliotecas MPP: Kamel para imagens (Compose MPP) no Android; [[Ktor]]/[[SQLDelight]] no shared.
- MVVM: ViewModel Android consome o domínio; no iOS, um Facade simplifica o consumo SwiftUI.

## Limitações/Notas
- iOS: Compose Multiplatform para iOS ainda evolui; para este desafio, privilegiamos [[SwiftUI]] no iOS e Compose no Android.
- Plataforma: quando performance/UX nativa são mandatórias, manter UI nativa por plataforma e compartilhar apenas domínio/dados.

## Ligações
- [[KMP]] · [[Kotlin]] · [[Android]] · [[iOS]] · [[SwiftUI]] · [[MVVM]] · [[Ktor]] · [[SQLDelight]]

