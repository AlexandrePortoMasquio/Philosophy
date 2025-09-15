---
title: Ecossistema Kotlin
updated: 2025-09-15
---

## Definição

O ecossistema Kotlin é o conjunto integrado de linguagem, [[Compilador]], ferramentas de build, bibliotecas oficiais e práticas que sustentam o desenvolvimento em Kotlin em múltiplas plataformas. Abrange Kotlin/JVM (Android e backend), Kotlin/JS e Kotlin/Native, bem como distribuição de artefatos e integração com IDEs; o objetivo é oferecer uma base coerente para escrever, testar e distribuir software com segurança e clareza.

## Como funciona

A toolchain organiza projetos por conjuntos de fontes (source sets) e plugins Gradle, permitindo partilha de código onde é estável e variação onde é necessária. As bibliotecas “kotlinx” (coroutines, serialization, datetime, entre outras) fornecem capacidades transversais; o [[KMP]] estrutura um núcleo comum (`commonMain`) e implementações específicas (`androidMain`, `iosMain`) por meio de `expect/actual`. Para interface, o Compose oferece opções nativas e multiplataforma, preservando a ligação com APIs de cada ambiente quando apropriado.

## Relações
[[Kotlin]] · [[Desenvolvimento de Software]] · [[KMP]] · [[Linguagem de Programação]]
