---
title: Lista (Software)
tags: [estrutura de dados, software]
created: 2025-09-15
updated: 2025-09-15
---

## Definição

Lista é uma estrutura de dados linear que organiza elementos em ordem e permite percorrê‑los sequencialmente, além de acessar posições conforme a implementação. Duas famílias predominam: arranjo dinâmico (cresce por redimensionamento) e lista encadeada (nós ligados por referências). A finalidade é manter uma sequência flexível para inserções, remoções e iterações, preservando a ordenação definida.

Relaciona‑se ao estudo de [[Ciência da Computação/Estruturas de Dados/Estruturas de Dados|Estruturas de Dados]]. Exemplo cotidiano: uma playlist em que a ordem dos itens importa e pode ser reordenada sem alterar o conteúdo de cada música.

## Funcionalidade

Operações típicas incluem adicionar e remover no fim, início ou meio; acessar um elemento pela posição; percorrer todos os elementos aplicando uma função; e buscar um valor. Em arranjos dinâmicos, o acesso por índice é direto e rápido, enquanto inserções no meio deslocam elementos; o crescimento ocorre por redimensionamentos ocasionais. Em listas encadeadas, inserções e remoções próximas a um nó conhecido são rápidas, enquanto o acesso posicional requer caminhada sequencial.

A escolha entre variantes depende do padrão de uso: acesso aleatório frequente favorece arranjos dinâmicos; alterações internas frequentes, com pouca necessidade de acesso por índice, favorecem listas encadeadas. Em interfaces gráficas, listas virtuais combinam a estrutura lógica com técnicas de renderização sob demanda para manter fluidez.

## Casos de Uso

Coleções que preservam ordem de inserção ou uma ordenação definida: itens de menu, resultados paginados, histórico de navegação, logs e playlists. Em aplicações móveis, telas de lista e feeds organizam conteúdo rolável; a fluidez pode ser analisada com ferramentas como [[Perfetto]] ao identificar trechos que causam engasgos. Quando há políticas específicas de acesso, estruturas afins podem ser preferidas, como [[Ciência da Computação/Estruturas de Dados/Pilhas|Pilhas]] (LIFO) e [[Ciência da Computação/Estruturas de Dados/Filas|Filas]] (FIFO).

