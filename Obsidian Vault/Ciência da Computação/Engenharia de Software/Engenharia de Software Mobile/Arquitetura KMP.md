---
title: Arquitetura KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, kmp, arquitetura]
created: 2025-08-28
updated: 2025-08-29
---

## Mapa Rápido
- Acima: [[../Arquitetura de Software|Arquitetura de Software]] 
- Lado: [[KMP]] · [[Android]] · [[iOS]] · [[Multiplataforma]]
- NÃO conectar com filosofia

## Arquiteturas Profissionais (como aplicar)
- Camadas Limpa/Clean: `:core:domain` (entidades/UseCases) e `:core:data` (repositórios, fontes local/remota). Shared (KMP) abriga ambas; apresentação fica nas apps.
- MVVM + UDF: Android com ViewModel + StateFlow/Reducer; iOS com ObservableObject/State. Use cases orquestram regras; repositórios abstraem dados.
- MVI (quando fizer sentido): único estado imutável por tela, intents, reducer e efeitos. Útil em flows complexos.
- Modularização por feature: `:feature:catalog` etc., dependem de `:core:*` via interfaces; facilita testes e evolução.
- DI: Koin core no shared (contratos e wiring leve), Koin Android apenas na apresentação; iOS faz composition root em Swift.
- Offline‑first: RemoteDataSource (Ktor) + Local (SQLDelight); política de hidratação (insertOrReplace), [[TTL]]/refresh.
- Ports/Adapters: contratos (interfaces) no domínio (`Repository`, `UseCase`) e implementações concretas em data/features; bordas fazem a composição via DI.

## Ideia
- Separar lógica de domínio/dados em módulos KMP compartilhados, mantendo UI nativa por plataforma.
- Minimizar atritos de interop (Swift/ObjC) com APIs estáveis e conversões claras de tipos.

## Estrutura Recomendada
- Shared (KMP): módulos `:core:domain`, `:core:data` (commonMain + expect/actual para IO/crypto)
- Android app: módulos `:app` + features; DI com Koin, Navigation Compose.
- iOS app: integra XCFramework do módulo compartilhado; DI/estado locais da plataforma.

## Fluxos e Contratos
- UDF no lado Android; expor fluxos (Flow/StateFlow) no shared com adaptadores para Swift Combine.
- Contratos estáveis (DTOs/resultados) mantêm identidade entre plataformas.

## App.kt vs KmpApp.kt (Android)
- KmpApp.kt: classe `Application` do Android. Inicializa DI (Koin), logging e providers globais (ex.: `SqlDriver`). Ponto único de configuração do processo.
- App.kt: composable raiz (ex.: `RootApp`) chamado por `MainActivity#setContent { ... }`. Define tema, navegação e estado de UI.
- Padrão profissional: manter ambos com nomes claros — `MyAppApplication` (Application) e `RootApp` (UI raiz). Manifest: `android:name=".MyAppApplication"`.

## Testes e CI/CD
- Testes unitários em `commonTest`; instrumentados por plataforma.
- Publicação do shared: Maven/XCFramework; versões semânticas; automação em CI.

## Riscos
- Supercompartilhar (UI/interop complexos) — manter fronteiras nítidas.
- Latência/bridging — medir e ajustar interfaces.

## Ligações
- [[KMP]] · [[Multiplataforma]] · [[Android]] · [[../Arquitetura de Software|Arquitetura de Software]] · [[Engenharia de Software/Testes|Testes]]

## Princípios SOLID no KMP
- SRP — Princípio da Responsabilidade Única (Single Responsibility Principle): módulos e classes com papéis únicos (ex.: `UseCase`, `Repository`, `Mapper`); UI nativa sem regras de negócio.
- OCP — Princípio do Aberto/Fechado (Open-Closed Principle): evoluir por extensão (novos `UseCase`/handlers) e `sealed class Result` para novas variantes sem modificar chamadores.
- LSP — Princípio da Substituição de Liskov (Liskov Substitution Principle): contratos testáveis; fakes substituem implementações reais sem quebrar invariantes (ex.: retries, cache policy).
- ISP — Princípio da Segregação de Interfaces (Interface Segregation Principle): interfaces focadas por feature (evitar um repositório único onipotente); separar portas de leitura/escrita quando útil.
- DIP — Princípio da Inversão de Dependência (Dependency Inversion Principle): shared depende de interfaces (`expect` ou interfaces puras); injeção nas bordas Android/iOS fornece `actual` concretos.

### Enforcement
- Limites de pacote/módulo; visibilidade restrita; regras do Gradle (dependency constraints).
- Testes de substituição (LSP) e contratos de API; análise estática e lint.

## Regras de Dependência
- Shared (KMP) — Domínio/Modelos: sem AndroidX/Swift; apenas Kotlin multiplataforma (stdlib, coroutines, serialization).
- Shared (KMP) — Dados: apenas libs KMP (Ktor/SQLDelight) — zero APIs específicas de plataforma.
- Apresentação (plataforma): Compose no Android e SwiftUI no iOS; adaptação/DI nas bordas.

## Boas Práticas de Nomenclatura e Módulos
- Mantenha os nomes do template (ex.: `:composeApp`) salvo exigência explícita; evite renomear módulos sem necessidade.
- Composable raiz em Android: `RootApp`/`MainApp`; classe `Application`: `MyAppApplication`.
- Shared sem específicos de plataforma: nada de AndroidX/Swift/Core no shared; engines/drivers apenas por source sets.

## Escolhas de Bibliotecas (racionais curtos)
- [[SQLDelight]]: um único schema/queries no Shared; APIs tipadas; ideal para offline-first. Drivers entram só nas bordas (Android/iOS).
- [[Napier]]: logging KMP leve; evita `println`/logs específicos de plataforma no Shared; suficiente para diagnóstico e observabilidade básica.

## [[ADR]]s (Decisões Registradas)
- DI: Koin no shared (wiring leve) e na apresentação Android; iOS com composition root. Consequência: sem codegen, build mais rápido; flexível para KMP.
- Rede/JSON: Ktor + kotlinx.serialization. Consequência: binário menor, integração multiplataforma direta.
- Persistência: SQLDelight. Consequência: tipagem forte e queries portáveis; drivers por plataforma nas bordas.
- Logging: Napier. Consequência: observabilidade mínima multiplataforma sem acoplamento.

## Contratos de Erro e Estados de UI
- `sealed interface DomainError { object Network; object Timeout; object NotFound; data class Unknown(val cause: String) }`
- `sealed interface UiState { object Loading; object Empty; data class Content(...); data class Error(val error: DomainError) }`
- Guidelines:
  - Nunca propagar exceções cruas para UI; mapear para `DomainError`.
  - Estados sempre imutáveis; transições via reducer; efeitos (navegação/toast) separados.


## Política Offline‑first
- [[TTL]]: 24h; invalidação por versão de schema ou logout. TTL = tempo de vida do cache antes de solicitar refresh.
- Refresh: manual (pull‑to‑refresh) e automático em segundo plano se rede disponível.
- Reconciliação: `insertOrReplace` por chave primária; idempotência nos repositórios.
- Erros: backoff exponencial; timeout padrão (ex.: 5s) e timeouts dedicados por rota sensível.

## Matriz de Testes
- commonTest: use cases + repositórios com driver em memória e fakes de rede.
- Android: UI (Compose), navegação e DAO instrumentado (se necessário).
- iOS: smoke tests consumindo o framework compartilhado.
