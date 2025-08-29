---
title: commonMain
tags: [kmp]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Source set padrão do KMP onde fica o código compartilhado entre plataformas (Shared): modelos, use cases, repositórios etc.

## shared vs commonMain
- `shared` costuma ser o nome do módulo Gradle que contém o código multiplataforma; `commonMain` é o source set dentro desse módulo. O padrão do KMP é o nome `commonMain`.
