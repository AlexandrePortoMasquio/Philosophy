---
title: Classe (Software)
tags: [engenharia de software, oo]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- A Classe está para o [[Objeto (Software)]] como a [[Forma]] está para o [[Objeto]] [[Concreto]].
- Molde de objetos com estado e comportamento; define invariantes e contratos. Em linguagens OO, organiza coesão e encapsula variáveis/operadores sob um contexto único.

## Princípios
- Encapsulamento: exponha intenções (métodos), oculte detalhes; imutabilidade quando possível.
- Coesão alta, acoplamento baixo: responsabilidade única (ver [[Princípios SOLID]] – SRP).
- Abstração vs. implementação: programe contra interfaces; prefira composição a herança profunda.

## Padrões de uso
- Entidades/Value Objects no domínio; Services/UseCases para orquestração; Adapters/Gateways para bordas.
- Em Kotlin: `data class` para valores imutáveis, `sealed` para hierarquias fechadas, `object` para singletons.

## Armadilhas
- God classes (muitas responsabilidades), herança frágil, estados inconsistentes (falta de invariantes), violação de encapsulamento.

## Ligações
- [[Padrões de Projeto]], [[Engenharia de Software]], [[Kotlin]], [[Java]], [[Domain]].

