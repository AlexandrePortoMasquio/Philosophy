---
title: Arquitetura KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, kmp, arquitetura]
created: 2025-08-28
updated: 2025-08-28
---

## Mapa Rápido
- Acima: [[../Arquitetura de Software|Arquitetura de Software]] 
- Lado: [[KMP]] · [[Android]] · [[iOS]] · [[Multiplataforma]]
- NÃO conectar com filosofia

## Ideia
- Separar lógica de domínio/dados em módulos KMP compartilhados, mantendo UI nativa por plataforma.
- Minimizar atritos de interop (Swift/ObjC) com APIs estáveis e conversões claras de tipos.

## Estrutura Recomendada
- shared: `:core:domain`, `:core:data` (commonMain + expect/actual para IO/crypto)
- Android app: módulos `:app` + features; DI com Hilt, Navigation Compose.
- iOS app: integra XCFramework do módulo compartilhado; DI/estado locais da plataforma.

## Fluxos e Contratos
- UDF no lado Android; expor fluxos (Flow/StateFlow) no shared com adaptadores para Swift Combine.
- Contratos estáveis (DTOs/resultados) mantêm identidade entre plataformas.

## Testes e CI/CD
- Testes unitários em `commonTest`; instrumentados por plataforma.
- Publicação do shared: Maven/XCFramework; versões semânticas; automação em CI.

## Riscos
- Supercompartilhar (UI/interop complexos) — manter fronteiras nítidas.
- Latência/bridging — medir e ajustar interfaces.

## Ligações
- [[KMP]] · [[Multiplataforma]] · [[Android]] · [[../Arquitetura de Software|Arquitetura de Software]] · [[Engenharia de Software/Processos|Processos]] · [[Engenharia de Software/Testes|Testes]]

## Princípios SOLID no KMP
- SRP — Princípio da Responsabilidade Única (Single Responsibility Principle): módulos e classes com papéis únicos (ex.: `UseCase`, `Repository`, `Mapper`); UI nativa sem regras de negócio.
- OCP — Princípio do Aberto/Fechado (Open-Closed Principle): evoluir por extensão (novos `UseCase`/handlers) e `sealed class Result` para novas variantes sem modificar chamadores.
- LSP — Princípio da Substituição de Liskov (Liskov Substitution Principle): contratos testáveis; fakes substituem implementações reais sem quebrar invariantes (ex.: retries, cache policy).
- ISP — Princípio da Segregação de Interfaces (Interface Segregation Principle): interfaces focadas por feature (evitar um repositório único onipotente); separar portas de leitura/escrita quando útil.
- DIP — Princípio da Inversão de Dependência (Dependency Inversion Principle): shared depende de interfaces (`expect` ou interfaces puras); injeção nas bordas Android/iOS fornece `actual` concretos.

### Enforcement
- Limites de pacote/módulo; visibilidade restrita; regras do Gradle (dependency constraints).
- Testes de substituição (LSP) e contratos de API; análise estática e lint.
