---
title: Domain (KMP)
tags: [kmp, domain]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Camada central de regras/modelos independente de plataforma. No KMP, o domínio define entidades, contratos (ports), casos de uso, tipos de erro/resultado, sem referências a Android/iOS/infra.

## Por que sealed interface DomainError no KMP
- Contrato explícito e estável: a UI (Android/SwiftUI) lida com variantes conhecidas (Network/Timeout/NotFound/Unknown), aplicando OCP. Como novas variantes não quebram chamadores? Porque o contrato exige que os consumidores:
  1) tratem apenas o subconjunto “estável” (Network/Timeout/NotFound) e
  2) tenham um `else`/`default` mapeando qualquer outra variante para uma experiência genérica (ex.: mensagem padrão), tipicamente via `Unknown`.
  Assim, adicionar `DomainError.PaymentRequired` no core não força mudanças em telas já publicadas: o `when` não-exaustivo com `else` mantém compatibilidade binária/semântica. Para fluxos que exigem exaustividade, o guideline é centralizar a normalização em um mapper (`DomainError → UiError`) exaustivo, enquanto as UIs dependem apenas do resultado mapeado.
- Testabilidade e LSP: fakes/stubs simulam erros tipados sem depender de exceções específicas de plataforma; [[Consumidor (Software)|consumidores]] testam por padrão de correspondência, não por mensagens.
- Interop iOS: evita propagar exceções do Kotlin/Native pela ponte; expõe um tipo de erro claro para Swift (checável por tipo), melhor do que “throw” cruzando o boundary.
- UX consistente: mapeamento de `DomainError → UiState.Error` padroniza mensagens/retry e facilita i18n.

## Padrão
- `sealed interface DomainError { object Network; object Timeout; object NotFound; data class Unknown(...) }`.
- Sempre converta exceções de borda (Ktor/DB) para `DomainError` nos repositórios/adapters.
- Nunca lançar exceções cruas para a UI; representar erro como parte do estado/result.
## Resumo para README (cliente)
- Definimos `DomainError` como sealed interface para explicitar erros de domínio independentes de plataforma, garantindo tipagem forte (Kotlin/Swift) e mapeamento consistente para estado de UI. OCP é obtido tratando um núcleo estável de variantes e um caminho `Unknown` para extensões futuras; assim novas variantes não quebram apps existentes. Exceções de infraestrutura são convertidas no boundary dos repositórios, e a UI só conhece `DomainError` e um mapper `DomainError → UiState.Error` com mensagens/retry padronizados.

## Elementos do domínio (no desafio)
- Entidades: `CatalogItem` e correlatos (valores puros, sem anotações de infra).
- Ports: `CatalogRepository`, `RemoteDataSource`, `LocalDataSource`, interfaces de [[UseCase|casos de uso]].
- Resultados/Erros: `AppResult<T>`, `DomainError` (superfície estável para a UI).

## Fronteiras e Adapters
- Adapters (`CatalogRepositoryImpl`, `KtorRemoteDataSource`, `SqlDelightLocalDataSource`) vivem fora do domínio e implementam as [[Port|portas]].
- [[Facade]] expõe API iOS amigável; [[Adapter]] e [[Port]] isolam infra/tecnologia do domínio.

## Ligações
- [[Port]] · [[Adapter]] · [[Facade]] · [[Ciência da Computação/Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]]
