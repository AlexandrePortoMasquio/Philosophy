---
title: Custo (Algoritmo)
updated: 2025-09-28
---

## Definição
Custo, em algoritmos, é a medida dos recursos exigidos por uma execução para uma entrada dada. Os eixos usuais são tempo (número de passos efetivos) e espaço (memória adicional utilizada), podendo incluir outros recursos conforme o contexto. A avaliação pode considerar pior caso, caso médio ou melhor caso e, em análise assintótica, descreve a ordem de crescimento ao variar o tamanho da entrada.

## Derivação
O conceito surge da necessidade de comparar procedimentos independentemente de detalhes de máquina: modela-se o passo elementar, contam-se operações e estima-se memória. A formalização assintótica (p.ex., [[Notação Big O]]) abstrai constantes e termos menores para evidenciar a tendência dominante, enquanto medições empíricas registram o comportamento concreto sob implementações e ambientes específicos.

## Relações
Relaciona-se a [[Algoritmo]] (procedimento), à classificação assintótica por [[Notação Big O]] e a medidas de descrição como [[Complexidade de Kolmogorov]] quando o foco recai sobre a compressibilidade de representações. Exemplo cotidiano: buscar um nome em lista desordenada tende a custo proporcional ao tamanho da lista; em lista ordenada com busca apropriada, o custo cresce como o logaritmo do tamanho.

## Posicionamentos
Vantagens: fornece critério comparável para escolha de procedimentos e orienta projetos ao tornar explícitos os trade-offs entre tempo e memória. Limites: classes assintóticas podem ocultar constantes relevantes, efeitos de hardware e distribuições reais de entrada. A moderação recomenda declarar o modelo de custo e o regime (pior/médio/melhor caso), combinar análise com experimentação e justificar quando otimizar por tempo, por espaço ou por equilíbrio entre ambos.

