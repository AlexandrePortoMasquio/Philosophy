---
title: Desafio Técnico KMP
tags: [mobile, kotlin, kmp, desafio técnico, arquitetura]
created: 2025-08-28
updated: 2025-08-28
---


## Requisitos
* ## Requisitos
* Mobile App - Take Home Assignment You should supply the code for review, be ready to reference it for the follow-up technical interview, and be ready to present the code via Screen Share. The purpose of this assignment is to provide us with a sample of how you structure your software and what architectural approach you will implement. It should be representative of what you would do on a professional level. It should be representative of what you would do as a professional during your day to day on the job. Please take the time to review the grading criteria below. How will it be graded?  Solution works.  Code is clean, well-written, easy to read and contains documentation.  Functionally works and satisfies the requirements below.  Thoughtful design and user experience is a plus.  Code is unit tested. Other kinds of tests will be considered pluses. We incentivize you to perform mindful choices in your software solution and document them in a READ ME, so the evaluators can follow your train of thought. If you cannot meet all the requirements (due to time constraints or any other reasons), be sure to implement that as well. If you provide a list of things you would pick to implement next if you were to maintain this project for a long-time, that will be taken as a plus. Take Home Assignment – Local Sake Shops (Native Apps Android and iOS ) For this assignment, you will build a simple app that allows the user to see 1) a screen with a list of local sake shops and 2) a details screen for a specific sake shop. Requirements The data is going to be supplied in JSON format. The list page should contain items with sake shop names, address, and star ratings. Whenever a sake shop from the list is tapped, the user should be directed to the details page of that shop. The details page should contain details about the sake shops, including: • Shop name. • Shop picture. • A brief description. • A rating in stars. • Address (clickable, should open address in a Maps app or browser). • A button or link to visit the shop's website in default web browser or in a custom tab. Instructions 1. Build at least one component that displays all items from the supplied JSON data you got together with this assignment. 2. You will be evaluated based on at least some of the following: a. Software architecture and solution design. b. Re-usability of your solution (could someone re-implement your solution easily for a different type of data / different API? Could a Web version be built reusing your entities and use cases?). c. Good UX and UI will be considered pluses, but you don't need to spend a very long time pixel-perfecting the look and feel (we don't expect you to be a designer). Follow material design guidelines and you're good. d. Other factors include: any tests included, component structure and standards, performance and stability, etc. 3. You can either use Kotlin and Swift UI. 4. (Plus) You can use hybrid tools like Kotlin multiplatform for the business and data layers. If you want to do so, clone this project and use it as base. Note: UIKit submissions will not be accepted. Submission Your app should be able to run in simulators. Please zip the project folder (run ./gradlew clean before zipping) and be sure to include in your README how to set up dependencies if your solution requires it. It would be great if you could also include an APK file if it's an Android app.

## Ideia
- Planejar a arquitetura de um projeto Kotlin Multiplatform (KMP) para um desafio técnico, priorizando clareza de limites, testabilidade e entrega rápida sem comprometer a qualidade.
- Compartilhar lógica de domínio e dados; manter UI nativa por plataforma. Tornar explícitos os trade-offs e o plano de execução.

## Suposições do Desafio
- App exibe lista e detalhe de entidades vindas de uma API pública (p.ex., REST/JSON), com cache local e modo offline‑first.
- Requisitos mínimos: erro tratável (mensagens e retry), busca/filtragem local, indicador de loading, acessibilidade básica.
- Entrega: código versionado, instruções de build, testes cobrindo regras de negócio, demo funcional em Android e (opcional) iOS.

## Objetivos e Métricas
- Entregabilidade: setup em ≤ 10 min, build reprodutível.
- Qualidade: cobertura de regras de negócio ≥ 70% no módulo shared; lints sem erros.
- UX: tempo de 1º carregamento ≤ 1s com cache; ≤ 3s a frio com rede média.
- Estabilidade: zero crashes conhecidos; taxas de erro instrumentadas.

## Arquitetura Proposta
- Shared (KMP):
  - Módulos: `:shared:core:domain`, `:shared:core:data`, `:shared:feature:catalog`.
  - Domain: casos de uso, entidades e invariantes; erros tipados; orquestra políticas offline‑first.
  - Data: repositórios, fontes remota (Ktor) e local (SQLDelight); mapeadores; políticas de cache.
  - Expect/Actual: relógio, storage seguro, reachability, logger.
- Android:
  - App `:androidApp` + `:feature:*` finas (UI Compose, ViewModel, navegação). DI: Hilt.
  - Fluxo UDF: intents → reducer → state (StateFlow). Observabilidade: Timber + Crashlytics (stubável).
- iOS:
  - SwiftUI + Combine; integração via XCFramework do shared. Adaptadores de Flow → Publisher; DI local (p.ex., Factory).

## Fluxos de Dados (alto nível)
- UI → Intent → Caso de Uso → Repositório → (Remote/Local) → Model → Estado → UI.
- Sincronização: Startup → hidratar cache → refresh em segundo plano (se rede disponível) → reconciliar diffs.

## Decisões e Trade-offs
- JSON: kotlinx.serialization pela integração multiplataforma (evitar reflection e reduzir binário).
- Network: Ktor Client + engines por plataforma.
- Persistência: SQLDelight (schema único, código gerado multiplataforma).
- Concurrency: coroutines/Flow no shared; limite de paralelismo configurável. Em iOS, expor APIs sem suspensão no boundary.
- DI: construtores no shared; Hilt/Koin apenas na borda Android; em iOS, composição manual.

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
