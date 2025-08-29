---
title: Reatividade
tags: [conceitos, reatividade, streams, kmp]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Modelo em que mudanças de dados propagam-se automaticamente para os [[Consumidor de Dados|consumidores]], via streams/observáveis (ex.: `Flow`, `Publisher`).
- Foca em declarar dependências de dados e não em orquestrar manualmente callbacks/atualizações.

## Por que usar no [[KMP]]
- Unifica lógica assíncrona em `commonMain` com `kotlinx.coroutines.flow` e expõe um contrato único para Android/iOS.
- Mapeia naturalmente para UIs declarativas: Compose e [[SwiftUI]] observam estado e re-renderizam.
- Facilita tratamento padronizado de estados (loading/empty/content/error) como `sealed class`.

## Como usar no KMP
- Shared: expor `StateFlow<UiState>`/`Flow<DomainEvent>`; orquestrar IO com coroutines e cancelamento estruturado.
- Android: coletar em `Lifecycle`/Compose, convertendo em `State` com `collectAsStateWithLifecycle`.
- iOS: adaptar para Combine (`AnyPublisher`) ou closures; garantir entrega em main thread.

## Padrões
- Estado único por tela (`UiState` imutável); intents → reducer → novo estado (UDF/MVI).
- Backpressure/debounce para inputs (ex.: busca).
- Erros tipados propagados como parte do estado, não via exceção não tratada.

## Armadilhas
- Vazamentos por escopos incorretos (não cancelar jobs).
- Bloqueio de thread principal; sempre usar dispatchers adequados.
- Conversões erradas de nullability/coleções no boundary iOS.

## Ligações
- [[KMP]] · [[SwiftUI]] · [[Combine]]
