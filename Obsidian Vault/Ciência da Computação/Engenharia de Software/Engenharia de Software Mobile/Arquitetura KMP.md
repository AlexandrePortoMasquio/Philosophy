---
title: Arquitetura KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, kmp, arquitetura]
created: 2025-08-28
updated: 2025-08-28
---

## Mapa Rápido
- Acima: [[../Arquitetura de Software|Arquitetura de Software]] · [[../../Linguagens de Programação/Linguagens de Programação|Linguagens de Programação]]
- Lado: [[KMP]] · [[Android]] · [[iOS]] · [[Multiplataforma]]
- Filosofia: [[Granularidade]] · [[Identidade]] · [[Controle]]

## Ideia
- Separar lógica de domínio/dados em módulos KMP compartilhados, mantendo UI nativa por plataforma.
- Minimizar atritos de interop (Swift/ObjC) com APIs estáveis e conversões claras de tipos.

## Estrutura Recomendada
- shared: `:core:domain`, `:core:data` (commonMain + expect/actual para IO/crypto)
- Android app: módulos `:app` + features; DI com Hilt, Navigation Compose.
- iOS app: integra XCFramework do módulo compartilhado; DI/estado locais da plataforma.

## Fluxos e Contratos
- UDF no lado Android; expor fluxos (Flow/StateFlow) no shared com adaptadores para Swift Combine.
- Contratos estáveis (DTOs/resultados) mantêm [[Identidade]] entre plataformas.

## Testes e CI/CD
- Testes unitários em `commonTest`; instrumentados por plataforma.
- Publicação do shared: Maven/XCFramework; versões semânticas; automação em CI.

## Riscos
- Supercompartilhar (UI/interop complexos) — manter fronteiras nítidas.
- Latência/bridging — medir e ajustar interfaces.

## Ligações
- [[KMP]] · [[Multiplataforma]] · [[Android]] · [[../Arquitetura de Software|Arquitetura de Software]] · [[Engenharia de Software/Processos|Processos]] · [[Engenharia de Software/Testes|Testes]]
