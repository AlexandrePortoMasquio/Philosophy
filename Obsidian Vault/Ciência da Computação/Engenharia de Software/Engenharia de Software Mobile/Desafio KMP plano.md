---
title: Desafio KMP — Plano de Execução
tags: [mobile, kmp, planejamento]
created: 2025-08-29
updated: 2025-08-29
---

## Objetivo
- Executar o desafio KMP com entrega rápida, arquitetura limpa, testabilidade e UX consistente on/offline, conforme requisitos documentados em [[Desafio Técnico KMP]].

## Passo a passo (ordem sugerida)
1) Preparar ambiente e abrir base
   - Validar JDK/Gradle/Android SDK/Xcode.
   - Abrir projeto clonado em `Obsidian Vault/Projetos/bimm-kmp-challenge-base`. A cada passo, testar o build.
2) Modularizar Shared
   - Criar `:shared:core:domain` e `:shared:core:data` (se ainda não existirem).
   - Adicionar deps KMP: coroutines, serialization, datetime.
   Testar o build.
3) Definir contratos de domínio
   - Entidades, invariantes, `sealed class Result` e `DomainError`.
   - Casos de uso (lista/detalhe/busca/local‑filter).
   - Separação ports/adapters: definir interfaces (ports) para `UseCase` e `Repository` no domínio; implementações concretas (adapters) ficam em data (ou features) e entram por DI.
4) Implementar dados/offline‑first
   - `RemoteDataSource` (Ktor + JSON) com timeouts/backoff.
   - Schema/queries SQLDelight; `LocalDataSource` e repositórios.
   - Política: hidratação inicial, TTL=24h, refresh em background, reconciliação idempotente.
5) DI e Logging no shared
   - Injeção por construtor; wiring leve (Koin core opcional).
   - Inicializar Napier por ambiente (debug/release).
6) UI Android (Compose)
   - ViewModel (UDF): intents → reducer → `UiState` (loading/empty/error/content).
   - Telas: lista (cards, busca local) e detalhe; navegação; acessibilidade básica.
7) iOS mínimo (SwiftUI)
   - Gerar XCFramework do shared.
   - Adapter Flow→Combine; telas lista/detalhe simples.
8) Testes
   - `commonTest`: use cases e repositórios com fakes/driver em memória.
   - AndroidTest: DAO e navegação/UI básica; iOS: smoke tests.
9) CI/CD e Artefatos
   - Pipeline (lint + testes + build XCFramework + APK debug).
   - Publicar artefatos nos jobs; badges opcionais.
10) Documentação e Entrega
   - README (setup ≤10min, build Android/iOS, troubleshooting).
   - Architecture.md (camadas/fluxos/ADRs curtas).

## Dependências/Notas
- Endpoint real ou mock versionado no repositório (substituível).
- DI Android: Koin (preferência); confirmar se Hilt é exigência do cliente.
