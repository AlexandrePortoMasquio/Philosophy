---
title: Domain (KMP)
tags: [kmp, domain]
created: 2025-08-29
updated: 2025-08-29
---

## Por que sealed interface DomainError no KMP
- Contrato explícito e estável: a UI (Android/SwiftUI) lida com variantes conhecidas (Network/Timeout/NotFound/Unknown), aplicando OCP (novas variantes não quebram chamadores). TODO como assim novas variantes não quebram chamadores? Explique.
- Testabilidade e LSP: fakes/stubs simulam erros tipados sem depender de exceções específicas de plataforma; [[Consumidor (Software)|consumidores]] testam por padrão de correspondência, não por mensagens.
- Interop iOS: evita propagar exceções do Kotlin/Native pela ponte; expõe um tipo de erro claro para Swift (checável por tipo), melhor do que “throw” cruzando o boundary.
- UX consistente: mapeamento de `DomainError → UiState.Error` padroniza mensagens/retry e facilita i18n.

## Padrão
- `sealed interface DomainError { object Network; object Timeout; object NotFound; data class Unknown(...) }`.
- Sempre converta exceções de borda (Ktor/DB) para `DomainError` nos repositórios/adapters.
- Nunca lançar exceções cruas para a UI; representar erro como parte do estado/result.

TODO copie isto para o readme do desafio, precisamos explicar para o cliente o que fizemos, como e por quê.