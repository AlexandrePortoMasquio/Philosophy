---
title: Adapter (KMP)
tags: [kmp, arquitetura, adapters]
created: 2025-08-31
updated: 2025-08-31
---

## Ideia
- Adaptador implementa uma [[Port|porta]] com uma tecnologia específica (HTTP, DB, plataforma) e faz a tradução necessária (DTO↔Entidade, erros de infra→`DomainError`).

## No desafio KMP
- `KtorRemoteDataSource` implementa `RemoteDataSource` com [[Ktor]] + `kotlinx.serialization`.
- `SqlDelightLocalDataSource` implementa `LocalDataSource` com [[SQLDelight]].
- `CatalogRepositoryImpl` implementa `CatalogRepository` (política offline‑first, mapeamento de erros).
- Mappers puros fazem DTO↔Domínio; [[Providers]] (fábricas) constroem adapters; `AndroidSqliteDriver`/`IosDI` injetam drivers/`baseUrl`.
- [[Facade]] `CatalogFacade` adapta `suspend/Flow` para callbacks Swift (não expõe corrotinas a SwiftUI).

## Por quê
- Substituibilidade: trocar HTTP/DB ou mock↔real sem tocar no domínio/UI.
- Limites claros: infra fica aqui; o [[Domain|domínio]] não conhece Ktor/SQL/Android/iOS.

## Ligações
- [[Port]] · [[Domain]] · [[Facade]] · [[Ciência da Computação/Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]]

