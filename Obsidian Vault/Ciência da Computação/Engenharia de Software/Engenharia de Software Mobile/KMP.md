---
title: KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, multiplatform]
created: 2025-08-28
updated: 2025-08-29
---

## Mapa Rápido
- Lado: [[Multiplataforma]] · [[Android]] · [[iOS]]
- Acima: [[Arquitetura de Software]] · [[Linguagens de Programação]]
- Abaixo: CI/CD (publicação de artefatos), testes, integração com apps

## Ideia
- KMP permite compartilhar código [[Kotlin]] entre [[Android]], iOS e outras plataformas via módulos com `commonMain` (expect) e implementações específicas (`actual`).
- Objetivo: reduzir duplicação de regras de negócio mantendo experiência nativa na UI.

## Quando usar
- Domínio com lógica substancial e estável (networking, cache, validação, casos de uso) e UI nativa específica.
- Equipes com proficiência em Kotlin e integração [[iOS]] (Interop Swift/ObjC).

## Relações Arquiteturais
- Camadas: módulo compartilhado (domínio/dados) e apps finos (UI nativa, DI, navegação).
- Limites claros (API do módulo) preservam [[Modularidade]] adequada e reduzem acoplamento.
- mapeamentos consistentes (DTOs ↔ modelos de UI), evitando drift entre plataformas.

## Ferramentas
* [[SQDelight]]
* [[Koin]]
* [[Napier]]

## Perguntas e Respostas
- shared vs commonMain: "shared" costuma ser o nome do módulo Gradle; `commonMain` é o source set dentro desse módulo. Padrão de mercado: o source set chama‑se sempre `commonMain`; o nome do módulo varia (ex.: `:shared`, `:core`).

## Tópicos
- Estrutura: [[commonMain]], `androidMain`, `iosMain`; bibliotecas: kotlinx.coroutines, serialization, [[Ktor]].
- Interop iOS: geração de framework, bridging de tipos (nullable, collections), performance de bridging.
- Persistência: multiplataforma (SQLDelight, Realm/KMM) e cache.
- Testes: unitários em comum, instrumentados por plataforma; contratos de API.
- Publicação: CI/CD para distribuir artefatos (Maven, XCFramework) e versionamento semântico.

## Riscos e Mitigações
- Dissonância de ciclos (Xcode/Gradle): automatizar com scripts e fastlane.
- Supercompartilhamento: manter UI e integrações específicas fora do módulo compartilhado.
- Interop: validar ponte de tipos com suites pequenas de prova.

## Ligações
- [[Multiplataforma]] · [[Android]] · [[iOS]] · [[Engenharia de Software/Processos|Processos]] · [[Engenharia de Software/Ferramentas|Ferramentas]] · [[Arquitetura de Software]] · [[Cyberia Web]]

## Padrões Profissionais (KMP)
- Shared-first: todo Model/Domain/Repository/Data/UseCases ficam em `commonMain` (libs KMP apenas). UI é específica por plataforma.
- HttpClient único (Ktor): instanciado no shared; engines (OkHttp/Darwin) entram só por source sets, sem `expect/actual`.
- SqlDriver por DI: injeção por construtor; drivers (Android/Native) fornecidos nas bordas (Android/iOS), não no shared.
- DI: Koin core no shared (contratos), Koin Android apenas na apresentação Android.
- Resultados: padronizar use cases com `sealed class` para estados/erros (OCP/UX).
- Mappers: explicitar Db→Domain e DTO→Domain (SRP/testes).

## Por que SQLDelight e Napier no KMP
- SQLDelight: cache offline-first com um único schema/queries no Shared; APIs tipadas geradas a partir de `.sq` evitam erros em runtime; funciona em Android e iOS apenas trocando o driver. Ver [[SQLDelight]].
- Napier: logging multiplataforma (KMP) simples e leve; direciona logs para Logcat no Android e NSLog no iOS; facilita observabilidade mínima sem acoplamento de plataforma. Ver [[Napier]].

## TODOs
- Definir `:androidApp` como nome do módulo (em vez de `:composeApp`).
- Adicionar `sealed class Result/DomainError` aos use cases.
- Implementar `RemoteDataSource` (Ktor + DTOs) e hidratação do cache (SQLDelight).
- Criar mappers explícitos (DTO→Domain, Db→Domain).
- Compor DI no iOS (fornecer `SqlDriver` e instâncias do shared).
- Especificar estratégia de i18n (EN default, PT-BR opcional).
