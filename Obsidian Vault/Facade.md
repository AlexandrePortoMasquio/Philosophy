---
title: Facade (KMP/iOS)
tags: [kmp, facade, ios]
created: 2025-08-31
updated: 2025-08-31
---

## Ideia
- Facade expõe uma superfície simples e coesa para consumidores externos. No KMP, é útil para dar uma API amigável ao iOS/Swift sem vazar detalhes de corrotinas/Flow.

## No desafio KMP
- `CatalogFacade` publica métodos como `getList(onSuccess, onEmpty, onError)` e `getDetail(id, ...)`, chamando casos de uso/repositório e convertendo `suspend/Flow` em callbacks.
- Consumido por ViewModels SwiftUI `@MainActor`, que atualizam `@Published` no main thread sem lidar com `Deferred/Flow`.

## Por quê
- Interop limpa: evita fricção de tipos de concorrência entre Kotlin/Native e Swift.
- Encapsulamento: mantém o [[Domain|domínio]]/regras estáveis; mudanças internas não quebram a API de app iOS.

## Ligações
- [[Domain]] · [[Port]] · [[Adapter]] · [[Ciência da Computação/Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]]

