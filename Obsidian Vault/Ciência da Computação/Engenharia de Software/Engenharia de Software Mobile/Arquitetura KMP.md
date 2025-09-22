---
title: Arquitetura KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, kmp, arquitetura]
created: 2025-08-28
updated: 2025-08-29
---
## Definição

Arquitetura KMP é o arranjo de [[Camadas (KMP)]], contratos e [[Modularização (KMP)|módulos]] necessários para compartilhar lógica de domínio e dados entre plataformas mantendo interfaces nativas e fronteiras claras. O núcleo compartilhado concentra modelos, regras e serviços expressos em `commonMain`; o código específico de alvo permanece nas bordas (Android/iOS/JS), onde se realizam composições, integrações e políticas próprias de plataforma.

O objetivo é maximizar coerência e reutilização sem sacrificar experiência nativa: variações inevitáveis ficam encapsuladas por `expect/actual` e adaptadores; dependências invertem‑se a favor de interfaces do domínio; contratos estáveis (tipos, erros, fluxos) permitem testes comuns e evolução independente das implementações de cada alvo.

## Princípios

Separar comum de específico e proteger o comum de detalhes de plataforma; depender de contratos do domínio (não de implementações), aplicando inversão e segregação de interfaces; limitar a superfície das bordas com adaptadores `expect/actual` e dados imutáveis ao atravessar fronteiras. Testabilidade guia o desenho: regras ficam testáveis em `commonTest`; integrações são exercitadas por alvo com dublês mínimos. Medir interop e latência orienta escolhas sobre o que compartilhar e o que manter local à plataforma.

## Padrões de Arquitetura KMP

* [[MVVM]]
* [[Clean Architecture]]
* MVI
* UDF (Fluxo Unidirecional)
* Ports and Adapters (Hexagonal)


## Mapa Rápido
- Acima: [[../Arquitetura de Software|Arquitetura de Software]] 
- Lado: [[KMP]] · [[Android]] · [[iOS]] · [[Multiplataforma]]
- NÃO conectar com filosofia

## Arquiteturas Profissionais (como aplicar)
- Camadas Limpa/[[Clean Architecture]]: `:core:domain` (entidades/UseCases) e `:core:data` (repositórios, fontes local/remota). Shared (KMP) abriga ambas; apresentação fica nas apps.
- MVVM + UDF: Android com ViewModel + StateFlow/Reducer; iOS com ObservableObject/State. Use cases orquestram regras; repositórios abstraem dados.
- MVI (quando fizer sentido): único estado imutável por tela, intents, reducer e efeitos. Útil em flows complexos.
- Modularização por feature: `:feature:catalog` etc., dependem de `:core:*` via interfaces; facilita testes e evolução.
- DI: Koin core no shared (contratos e wiring leve), Koin Android apenas na apresentação; iOS faz composition root em Swift.
- Offline‑first: RemoteDataSource (Ktor) + Local (SQLDelight); política de hidratação (insertOrReplace), [[TTL]]/refresh.
- Ports/Adapters: contratos (interfaces) no domínio (`Repository`, `UseCase`) e implementações concretas em data/features; bordas fazem a composição via DI.

## Camadas
- Camadas não são necessariamente [[Módulo|módulos]]: camada é um papel/limite arquitetural; módulo é uma unidade de build/empacotamento. Você pode ter camadas distintas dentro de um único módulo (via pacotes) ou mapear cada camada para um módulo quando o isolamento/compilação separada trouxer valor.
- Recomendações no KMP:
  - Pequeno/Desafio: manter `Domain` e `Data` como pacotes dentro do módulo `:shared` (menos overhead).
  - Médio/Grande: separar em `:shared:core:domain` e `:shared:core:data` para reforçar dependências e reduzir acoplamento.
- Camadas principais: [[Domain]] (entidades, casos de uso, contratos) e [[../../../Data Layer]] (repositórios, fontes local/remota, mapeadores).

## Ideia
- Separar lógica de domínio/dados em módulos KMP compartilhados, mantendo UI nativa por plataforma.
- Minimizar atritos de interop (Swift/ObjC) com APIs estáveis e conversões claras de tipos.
- TODO Como fazer [[Migração (Software)]] do app [[KMP]]

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

## Testes (MVP)
- Testes unitários em `commonTest`; instrumentados por plataforma quando útil.
- Publicação: gerar frameworks/APK localmente para validação; CI/CD fora do escopo do MVP.

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
