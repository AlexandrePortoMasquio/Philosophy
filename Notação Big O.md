---
title: Notação Big O
updated: 2025-09-28
---
[[Algoritmo]] ······················
## Definição

A [[Notação Big O]] descreve a ordem de crescimento do [[Custo (Algoritmo)|custo]] de um [[Algoritmo]] em função do tamanho da entrada, abstraindo constantes e termos de menor ordem. Expressa limites assintóticos superiores: indica como tempo ou espaço escalam quando a entrada aumenta, permitindo comparar procedimentos independentemente de implementações específicas.

## Funcionalidade
Funciona como linguagem comum para analisar desempenho: classifica algoritmos por classes de crescimento (O(1), O(log n), O(n), O(n log n), O(n²), …), evidenciando trocas entre tempo e memória. Recorre a modelos de custo e ao pior caso, caso médio ou melhor caso, conforme o problema e o critério adotado, mantendo foco na tendência dominante quando n é grande.

## Casos de Uso
É empregada na escolha entre abordagens (p.ex., busca linear O(n) versus busca em estrutura ordenada O(log n)), na avaliação de algoritmos de ordenação (O(n log n) típicos, versus O(n²) quadráticos) e na estimativa de recursos em sistemas. Em prática, complementa medições empíricas: a classe assintótica orienta o projeto; os dados concretos expõem constantes e efeitos de hardware. Uso moderado evita fetichizar a classe e ignora limites do domínio.

