---
title: Desafio Técnico KMP
tags: [mobile, kotlin, kmp, desafio técnico, arquitetura]
created: 2025-08-28
\12025-08-29
---


## Requisitos
* [[Desafio Técnico KMP - Requisitos]]

## Ideia
- Planejar a arquitetura de um projeto Kotlin Multiplatform (KMP) para um desafio técnico, priorizando clareza de limites, testabilidade e entrega rápida sem comprometer a qualidade.
- Compartilhar lógica de domínio e dados; manter UI nativa por plataforma. Tornar explícitos os trade-offs e o plano de execução.

## Suposições do Desafio
- App exibe lista e detalhe de entidades vindas de uma API pública (p.ex., REST/JSON), com cache local e modo offline‑first.
- Requisitos mínimos: erro tratável (mensagens e retry), busca/filtragem local, indicador de loading, acessibilidade básica.
- Entrega: código versionado, instruções de build, testes cobrindo regras de negócio, demo funcional em Android e (opcional) iOS.

## Objetivos e Métricas
- Entregabilidade: setup em ≤ 10 min, build reprodutível.
- Qualidade na arquitetura: demonstrar habilidade altamente profissional, de um sênior especialista, em estruturar um projeto KMP.
- Respeitar o máximo possível os requerimentos do teste, fornecidos pelo cliente.
- Demonstrar conhecimento profundo em KMP, usando ferramentas da melhor forma possível e atendendo o melhor possível a todos os requerimentos.
- Qualidade: cobertura de regras de negócio ≥ 70% no módulo shared; lints sem erros.
- UX: tempo de 1º carregamento ≤ 1s com cache; ≤ 3s a frio com rede média.
- Design bonito, bem acabado e intuitivo.
- Estabilidade: zero crashes conhecidos; taxas de erro instrumentadas.

## Arquitetura Proposta

## Regras de Dependência por Camada
- Shared (KMP) — Domínio/Modelos: apenas Kotlin multiplataforma (stdlib, coroutines, serialization); sem AndroidX, sem Swift/Objective-C.
- Shared (KMP) — Dados: apenas bibliotecas multiplataforma (Ktor/SQLDelight/etc.); nada de APIs Android/iOS.
- Apresentação (plataforma): Compose (Android) e SwiftUI (iOS); adapters traduzem modelos/domínio → UI.
- Shared (KMP):
  - Módulos: `:shared:core:domain`, `:shared:core:data`, `:shared:feature:catalog`.
  - Domain: casos de uso, entidades e invariantes; erros tipados; orquestra políticas offline‑first.
  - Data: repositórios, fontes remota (Ktor) e local (SQLDelight); mapeadores; políticas de cache.
  - Expect/Actual: relógio, storage seguro, reachability, logger.
- Android:
  - App `:androidApp` + `:feature:*` finas (UI Compose, ViewModel, navegação). DI: Koin (apresentação Android).
  - Fluxo UDF: intents → reducer → state (StateFlow). Observabilidade: Timber + Crashlytics (stubável).
- iOS:
  - SwiftUI + Combine; integração via XCFramework do shared. Adaptadores de Flow → Publisher; DI local (p.ex., Factory).

## Fluxos de Dados (alto nível)
- UI → Intent → Caso de Uso → Repositório → (Remote/Local) → Model → Estado → UI.
- Sincronização: Startup → hidratar cache → refresh em segundo plano (se rede disponível) → reconciliar diffs.

## UI
* Os itens deverão ser apresentados em cards, com bordas arredondadas, cores estilosas e com um bom design bonito.

## Decisões e Trade-offs
- JSON: kotlinx.serialization pela integração multiplataforma (evitar reflection e reduzir binário).
- Network: Ktor Client + engines por plataforma.
- Persistência: SQLDelight (schema único, código gerado multiplataforma).
- Concurrency: coroutines/Flow no shared; limite de paralelismo configurável. Em iOS, expor APIs sem suspensão no boundary.
- DI: construtores no shared; Koin apenas na borda Android; em iOS, composição manual.

## Testes
- commonTest: casos de uso e repositórios com fakes (HTTP/DB), teste de políticas offline‑first.
- AndroidTest: DAO/Room ou SQLDelight Android driver; navegação; snapshot de UI (opcional).
- iOS tests: unidades de integração com o framework compartilhado.

## CI/CD (mínimo viável)
- Jobs: lint + testes (common + Android), build XCFramework; publicação local (MavenLocal/artefato no repositório do projeto).
- Artefatos: APK debug e XCFramework.
- Gatilhos: push e PR.

## Backlog Inicial
1) Bootstrap projeto KMP (Gradle, módulos shared).
2) Definir contratos de API e modelos; implementar `data` + `domain` (lista/detalhe, busca, cache).
3) Android UI (lista/detalhe, estados, navegação); instrumentação básica.
4) iOS UI simples (lista/detalhe) consumindo shared.
5) Testes: unidade (shared) e instrumentados (Android); fixtures.
6) CI: lint, testes, build XCFramework, artefatos de release interno.

## Critérios de Aceitação
- Build do shared e apps funciona em ambiente limpo; instruções claras.
- Lista e detalhe operam online e offline; mensagens de erro e retry.
- Testes de domínio passando; cobertura reportada.
- Código modular, limites claros, sem dependências cíclicas; lints OK.

## Riscos e Mitigações
- Interop iOS (tipos nulos, coleções): criar camada de DTOs e adaptadores dedicados; testes focados no boundary.
- Supercompartilhamento: manter UI nativa e integrações no app; revisar dependências do shared.
- Tempo do desafio: priorizar backlog pelo caminho crítico (dados → domínio → Android UI → testes → iOS UI mínima).


## Perguntas (para confirmação)
- Qual é o endpoint/dataset JSON real e um exemplo de schema?
- Há restrições de design/branding para a UI (cores, fontes, ícones)?
- Targets: Android (minSdk/target/compile) e iOS (deployment target)?
- Restrições legais/privacidade (telemetria, PII) ou política de logs?
- Confirmar DI: Koin no Android (apresentação), composição manual no iOS e por construtor no shared.
- Plataforma de CI preferida (p.ex., GitHub Actions) e ambiente de build?
- Prioridades/timebox: performance vs cobertura de testes vs features?
- Idioma padrão da UI (EN/PT-BR) e necessidade de i18n?
- TTL/estratégia de cache offline e gatilhos de refresh?

## Respostas
- Endpoint/Schema: na ausência de endpoint oficial, forneceremos um mock JSON versionado no projeto e abstrairemos o acesso via `CatalogRepository`, permitindo troca por endpoint real sem alterar UI.
- Design/Branding: Material 3 básico, dark mode, acessibilidade; ícones do Material; sem branding específico.
- Targets: Android `compileSdk=34`, `targetSdk=34`, `minSdk=24`; iOS `deploymentTarget=iOS 16`.
- Privacidade/Logs: sem analytics; logs locais (Napier/Timber) anonimizados; nenhum PII além do dataset.
- DI: shared com Koin core por construtor; Android com Koin (apresentação); iOS com factories (composition root).
- CI: GitHub Actions (lint, testes `commonTest`/Android, build XCFramework e APK).
- Prioridades: entregabilidade e corretude > testabilidade > UX; performance após básicos.
- Idioma: EN por padrão; PT-BR opcional se tempo permitir; strings isoladas para futura i18n.
- Cache: offline-first com TTL 24h; refresh manual e em segundo plano quando rede disponível.

## Ferramentas e Dependências (KMP)
- Regras de acoplamento (camadas):
  - Domínio/Modelos: sem dependências específicas de Android/iOS. Apenas Kotlin padrão e libs multiplataforma necessárias (ex.: coroutines, serialization) — sem AndroidX, sem Swift.
  - Dados: apenas bibliotecas multiplataforma (Ktor, SQLDelight, datetime, logging KMP). Nenhuma API específica de plataforma.
  - Apresentação: específico por plataforma — Android (Compose + AndroidX) e iOS (SwiftUI + Combine).
- Build: Gradle 8.7; Kotlin 2.0.20; AGP 8.5.2.
- Shared (KMP) — Domínio (:core:domain):
  - kotlinx.coroutines 1.8.1 (suspend/Flow), kotlinx.serialization 1.6.3, kotlinx.datetime 0.6.0.
- Shared (KMP) — Dados (:core:data):
  - Ktor Client 2.3.8 (core, content-negotiation, serialization-json).
  - SQLDelight 2.0.2 (runtime + drivers por plataforma fornecidos na borda).
  - Napier 2.7.1 (logging multiplataforma).
- Apresentação Android:
  - Compose BOM 2024.08.00; activity-compose; lifecycle-viewmodel-compose.
  - Koin 3.x (koin-android, koin-androidx-compose) na apresentação Android.
  - Ktor engine OkHttp; SQLDelight Android driver.
  - Testes: junit4, androidx.test, compose-ui-test-junit4, turbine 1.0.0.
- Apresentação iOS:
  - SwiftUI + Combine.verificação no CI.

### Injeção de Dependência
- Shared (KMP): injeção por construtor, sem framework. Dependências entram como interfaces (ports) e são fornecidas nas bordas, mantendo testabilidade e portabilidade.
- Android: Hilt para compor os concretos (network, storage, logger) e conectar casos de uso/repositórios. Módulos por feature para escopo e isolamento.
- iOS: Composition Root com fábricas (factories) e inicialização explícita, sem framework, reduzindo atrito de interop.
- Limites: contratos no shared (interfaces/expect); implementations e actuals apenas nas plataformas.

### Propostas para impressionar o cliente
- Qualidade arquitetural: módulos bem delimitados (domain/data/shared features), UDF/MVVM na apresentação, contratos selados para erros/estados e aplicação dos Princípios SOLID (por extenso).
- Offline-first robusto: cache, hidratação inicial, refresh em segundo plano e reconciliação de diffs; UX consistente on/offline.
- Testabilidade: >70% de cobertura no shared, fakes/stubs para repositórios, testes de substituição (LSP), instrumentados no Android e smoke em iOS.
- Observabilidade e resiliência: logging estruturado, métricas básicas, tratamento padronizado de falhas (timeouts, backoff, circuit breaker).
- Acessibilidade e UX: navegação clara, estados visuais (loading/empty/error), dark mode, tamanhos dinâmicos de fonte.
- Reprodutibilidade/CI: README com setup ≤ 10 min, pipeline com lint+testes+XCFramework, artefatos (APK/XCFramework).
- Documentação de decisões: ADRs curtas (contexto → opções → decisão → consequências) e diagramas simples das camadas/módulos.

### Como o código será documentado
- README raiz: setup, execução e build Android/iOS; troubleshooting.
- Architecture.md: camadas, módulos, fluxos (mermaid), limites e trade-offs.
- ADRs: 1–2 páginas por decisão relevante (DI, offline-first, serialização, persistência).
- READMEs por módulo (shared/domain/data/features) com responsabilidades e dependências.
- Contratos de API: schema JSON de exemplo, erros e timeouts esperados.
- KDoc no shared para casos de uso, repositórios e modelos; geração opcional.
- Guia de testes: como rodar suites (commonTest/AndroidTest/iOS) e estratégia de fakes.
## Ligações
- [[KMP]] · [[Arquitetura KMP]] · [[Arquitetura Android]] · [[../Arquitetura de Software|Arquitetura de Software]] · [[Engenharia de Software/Testes|Testes]] · [[Engenharia de Software/Processos|Processos]]

## SOLID no Desafio (Plano de Implementação)
- SRP — Princípio da Responsabilidade Única (Single Responsibility Principle): módulos `:shared:core:domain`, `:shared:core:data` e `:shared:feature:catalog` com responsabilidades nítidas; cada `UseCase` com um objetivo único.
- OCP — Princípio do Aberto/Fechado (Open-Closed Principle): `sealed class CatalogResult { Success|Empty|NetworkError|Timeout }`; novas variantes não quebram chamadores; handlers registrados por extensão.
- LSP — Princípio da Substituição de Liskov (Liskov Substitution Principle): `CatalogRepository` tem fakes para testes de UI/domínio; substituição preserva contratos (ex.: políticas de retry/cache).
- ISP — Princípio da Segregação de Interfaces (Interface Segregation Principle): interfaces específicas (ex.: `ReadOnlyCatalogRepository` para telas somente leitura); separar comandos de consultas quando útil.
- DIP — Princípio da Inversão de Dependência (Dependency Inversion Principle): shared depende de `CatalogRepository` (interface); Android/iOS fornecem implementações via DI na borda.

### Tarefas Concretas
1) Definir interfaces do domínio e resultados `sealed` (DIP/OCP).
2) Implementar fakes/stubs do repositório e testes de substituição (LSP).
3) Quebrar interfaces gordas por caso de uso/consulta (ISP).
4) Isolar mapeadores/adaptadores por módulo (SRP) e restringir visibilidades.
5) Garantir extensão por composição (novos casos/handlers) sem editar código estabilizado (OCP).

### Critérios de Aceitação (SOLID)
- Inclusão de uma nova variante de erro requer apenas adicionar código (sem modificar contratos existentes).
- Substituir repo real por fake não altera cenários de teste (mesmo comportamento observado).
- Nenhuma interface com métodos não utilizados nas telas-alvo.
