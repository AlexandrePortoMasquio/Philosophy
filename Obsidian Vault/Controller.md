---
title: Controller
tags: [arquitetura]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Componente do MVC que recebe input e coordena View/Model. Em mobile, costuma virar um “God Object” se não for disciplinado.

## É usado no KMP?
- No núcleo compartilhado, não. Evitamos MVC/Controller no shared; adotamos MVVM/[[UDF]] com `UseCase`/`Repository` (ports) e UI reativa nas bordas.
- Android: embora exista `Activity`/`Fragment` (controladores de plataforma), a lógica fica em `ViewModel`; telas Compose observam estado.
- iOS: com SwiftUI não há `UIViewController` como controlador da lógica de tela; usamos `ObservableObject` + Combine consumindo o shared.

## Ligações
- [[MVC]] · [[MVP]] · [[ViewModel]]
