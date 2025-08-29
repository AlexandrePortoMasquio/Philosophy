---
title: KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, multiplatform]
created: 2025-08-28
updated: 2025-08-28
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
- Equipes com proficiência em Kotlin e integração iOS (Interop Swift/ObjC).

## Relações Arquiteturais
- Camadas: módulo compartilhado (domínio/dados) e apps finos (UI nativa, DI, navegação).
- Limites claros (API do módulo) preservam [[Modularidade]] adequada e reduzem acoplamento.
- mapeamentos consistentes (DTOs ↔ modelos de UI), evitando drift entre plataformas.

## Tópicos
- Estrutura: `commonMain`, `androidMain`, `iosMain`; bibliotecas: kotlinx.coroutines, serialization, Ktor.
- Interop iOS: geração de framework, bridging de tipos (nullable, collections), performance de bridging.
- Persistência: multiplataforma (SQLDelight, Realm/KMM) e cache.
- Testes: unitários em comum, instrumentados por plataforma; contratos de API.
- Publicação: CI/CD para distribuir artefatos (Maven, XCFramework) e versionamento semântico.

## Riscos e Mitigações
- Dissonância de ciclos (Xcode/Gradle): automatizar com scripts e fastlane.
- Supercompartilhamento: manter UI e integrações específicas fora do módulo compartilhado.
- Interop: validar ponte de tipos com suites pequenas de prova.

## Ligações
- [[Multiplataforma]] · [[Android]] · [[iOS]] · [[Engenharia de Software/Processos|Processos]] · [[Engenharia de Software/Ferramentas|Ferramentas]] · [[Arquitetura de Software]]
