---
title: Napier
tags: [kmp, logging]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Biblioteca de [[Logging]] multiplataforma para Kotlin Multiplatform (KMP), com API simples e direcionamento por plataforma (Logcat/NSLog/console).

## Por que usar no KMP
- Multiplataforma real: um único ponto de logging no Shared; sem `expect/actual` nem `println` ad hoc.
- Observabilidade mínima: registros de erro/info durante desenvolvimento e em produção (com controle de nível), sem acoplamento à plataforma.
- Leve e direto: suficiente para um desafio técnico; facilita troubleshooting de rede/cache sem puxar infra pesada.

## Integração (padrão)
- Shared: inicializa logger e usa `Napier.d/e` nos pontos críticos (network/cache/use cases).
- Android/iOS: direcionamento automático para Logcat/NSLog; pode customizar árvores de log.

## Alternativas
- Kermit (Touchlab): também KMP, com API semelhante; escolha de projeto. Napier atende bem pela simplicidade.
- Logger Android / NSLog: específicos de plataforma e aumentam acoplamento; evitados no Shared.


## Napier vs Kermit (resumo)
- Napier: API mínima, configuração simples, leve; ideal para desafios/projetos de referência.
- Kermit: API semelhante, integração com multiplataforma madura; ligeiramente mais funcionalidades utilitárias.
- Ambas funcionam; escolha por preferência/equipe. Este projeto usa Napier pela simplicidade.

## Exemplo de Inicialização
```kotlin
import io.github.aakira.napier.Napier

fun initLogging(debug: Boolean) {
    if (debug) Napier.base(DebugAntilog())
}
```
