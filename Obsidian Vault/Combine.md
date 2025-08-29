---
title: Combine
tags: [ios, reatividade, streams]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Framework reativo da Apple para composição de fluxos assíncronos (Publishers/Subscribers), com operadores (map, filter, debounce) e backpressure.

## Conceitos
- Publisher: produz valores ao longo do tempo (ou erro/completion).
- Subscriber: consome valores, com demanda controlada.
- Operators: constroem pipelines declarativos sobre streams.

## Relação com [[KMP]]
- Ponte com `Flow`: o shared expõe `kotlinx.coroutines.flow.Flow`/`StateFlow`; no iOS, adaptamos para `AnyPublisher`/`ObservableObject`.
- Estratégias de adaptação:
  - Expor no shared funções que aceitam callbacks (onEach/onCompletion), simplificando consumo em Swift.
  - Fornecer adaptadores (em Swift) que convertem `Flow` em `Publisher` usando o bridge de coroutines e agendamento no main runloop.

## Padrão prático
```swift
// Swift (iOS)
final class CatalogViewModel: ObservableObject {
    @Published private(set) var state: UiState = .loading
    private let sharedVm: SharedCatalogViewModel
    private var cancellables = Set<AnyCancellable>()

    init(sharedVm: SharedCatalogViewModel) {
        self.sharedVm = sharedVm
        sharedVm.statePublisher()              // adaptado do Flow
            .receive(on: RunLoop.main)
            .assign(to: &$state)
    }
}
```

## Boas práticas
- Encerrar stream ao desalocar tela/escopo; evitar vazamentos.
- Converter no Main Thread antes de tocar UI.
- Debounce de buscas/inputs para reduzir chamadas de rede.

## Ligações
- [[Reatividade]] · [[SwiftUI]] · [[KMP]]
