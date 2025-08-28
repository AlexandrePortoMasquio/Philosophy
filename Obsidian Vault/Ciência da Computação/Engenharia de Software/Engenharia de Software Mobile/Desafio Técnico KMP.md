---
title: Desafio Técnico KMP
tags: [mobile, kotlin, kmp, desafio técnico, arquitetura]
created: 2025-08-28
updated: 2025-08-28
---

## Mapa Rápido
- Acima: [[../Arquitetura de Software|Arquitetura de Software]] · [[../../Linguagens de Programação/Linguagens de Programação|Linguagens de Programação]]
- Lado: [[KMP]] · [[Arquitetura Android]] · [[Arquitetura KMP]] · [[Multiplataforma]] · [[Android]] · [[iOS]]
- Artefatos: ADRs · Módulos · Pipelines CI/CD · Critérios de Aceitação

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
