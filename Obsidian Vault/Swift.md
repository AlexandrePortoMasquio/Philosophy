---
title: Swift — Thread Safety
tags: [swift, ios, concorrência]
created: 2025-08-31
updated: 2025-08-31
---

## Ideia
- Swift moderno usa concorrência estruturada (async/await) + modelo de atores para segurança contra condições de corrida em nível de linguagem. Thread‑safety decorre de isolamento por ator, tipos `Sendable` e imutabilidade por padrão.

## Fundamentos
- Imutabilidade e value types: `struct`/`enum` (copy‑on‑write em coleções padrão) reduzem compartilhamento mutável.
- `Sendable`: tipos seguros para atravessar domínios de concorrência. Marcar tipos próprios como `Sendable` (ou `@unchecked Sendable` com cuidado).
- Atores: `actor` isola estado; só uma tarefa acessa mutabilidade do ator por vez. UI pertence ao `@MainActor`.
- Reentrância: um `await` dentro de um ator pode intercalar outras mensagens; proteger invariantes antes/depois do `await`.

## Padrões
- UI no `@MainActor`:
  - Anotar ViewModels/serviços de UI com `@MainActor` para garantir atualizações de tela no main thread.
  - Ex.: `@MainActor final class MyViewModel: ObservableObject { @Published var state: UiState = .idle }`
- Isolar serviços mutáveis em `actor`s:
  - `actor Cache { private var store: [Key:Value] = [:]; func put(...) { ... } func get(...) -> Value? { ... } }`
- Evitar estado global mutável; preferir injeção de dependências e instâncias confinadas a atores/filas seriais.
- Preferir funções puras/imutáveis para DTOs/transformações.

## Ferramentas de sincronização (quando ator não basta)
- `DispatchQueue` serial para recursos legados; `NSLock/os_unfair_lock` como último recurso (cuidado com deadlocks/inversão de prioridade).
- Swift Atomics (biblioteca) para contadores/flags atômicos simples.

## Erros comuns e como evitar
- Capturar `self` mutável em `Task {}` e modificar estado não isolado → usar `@MainActor`/atores ou `MainActor.run { ... }` para tocar UI.
- Aguardar (`await`) no meio de uma atualização de estado complexo dentro do ator → reorganizar para consolidar invariantes antes do `await`, ou dividir em dois métodos.
- Acessar coleções mutáveis a partir de múltiplas tasks → encapsular em ator/queue ou usar snapshot imutável.

## Exemplo (ViewModel com segurança de thread)
```
@MainActor
final class CatalogVM: ObservableObject {
  @Published var state: UiState = .loading
  private let facade: CatalogFacade  // vindo do KMP

  func load() {
    state = .loading
    facade.getList(
      onSuccess: { items in self.state = .content(items) },
      onEmpty:   { self.state = .empty },
      onError:   { _ in self.state = .error("Try again") }
    )
  }
}
```
- Nota: `@MainActor` garante que `state` é atualizado no main thread, mesmo que callbacks venham de threads distintos.

## Atores e reentrância
```
actor Counter {
  private var value = 0
  func next() -> Int { value += 1; return value }
  func nextAfterNetwork(client: Client) async throws -> Int {
    let current = value          // salvar estado local
    let delta = try await client.fetchDelta() // reentrante aqui
    value = current + delta      // reestabelecer invariante
    return value
  }
}
```
- Evitar depender de `value` logo após `await` sem capturar snapshot anterior.

## Interop com [[KMP]]
- Use [[Facade]] KMP para expor callbacks/assinaturas simples; consuma sob `@MainActor`.
- Evite manter referências KMP long‑lived em múltiplas threads; crie/capture localmente onde usar.
- Kotlin/Native (novo modelo de memória) reduz congelamento, mas mantenha regra: UI → `@MainActor`; tarefas de IO → `Task.detached`/atores isolados.

## Testes e diagnósticos
- Xcode Thread Sanitizer: detectar corridas de dados.
- XCTest async: `await` em testes; injetar dependências isoladas/atores fakes.

## Checklists
- [ ] Tipos que cruzam tasks são `Sendable`.
- [ ] Estado mutável isolado em ator/queue.
- [ ] UI anotada com `@MainActor`.
- [ ] Sem `await` no meio de atualização de invariantes.

## TODO List
* Faltou falar incluir tasks, cancellation, isolation.

## Ligações
- [[SwiftUI]] · [[iOS]] · [[KMP]] · [[Facade]]

