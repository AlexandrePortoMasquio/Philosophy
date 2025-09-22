---
title: Semântica (Programação)
updated: 2025-09-21
---
Derivado de [[Programação]]

## Definição

Semântica, em programação, é o estudo do significado de programas: o que um trecho de [[Código-Fonte]] faz quando executado, quais efeitos produz e sob quais condições. Distingue‑se de [[Sintaxe (Programação)]] (forma) por tratar do comportamento observável e das consequências de execução. Há diferentes modos de caracterizar esse significado: semântica operacional (regras de execução passo a passo), denotacional (interpretação matemática de programas) e axiomática (regras de correção como em lógicas de [[Hoare]]).

Exemplos simples ajudam a situar a ideia: avaliação de curto‑circuito em operadores lógicos, ordem de avaliação de argumentos, efeitos de exceções e do estado mutável, ou o que conta como comportamento indefinido. A semântica torna explícitas essas escolhas para permitir raciocínio, verificação e interoperabilidade entre componentes.

## Funcionalidade

Uma definição semântica dá critérios para equivalência de programas (quando duas implementações “fazem o mesmo”, elas têm a mesma semântica com sintaxes diferentes). Orienta otimizações que preservam comportamento e delimita contratos de execução (por exemplo, modelos de memória, tratamento de erros, não‑interferência entre threads). Em compilação, guia a transformação em [[Código de Alvo]]: apenas reescritas semântica e contextualmente seguras são aceitáveis (ver [[Compilação (Programação)]]).

Na prática de desenvolvimento, a semântica fundamenta especificações, testes e refatorações: descreve resultados esperados e casos limite, separa efeitos colaterais de cálculos puros e indica onde invariantes devem ser preservados. Diferenças semânticas entre plataformas exigem fronteiras claras e adaptação consciente quando o mesmo código é emitido para destinos distintos.

## TDD

Em [[Desenvolvimento Orientado a Testes]], casos e propriedades de [[Teste (Programação)|testes]] funcionam como fragmentos de especificação semântica: descrevem, em termos observáveis, o que o programa deve fazer sob condições dadas. Bons testes aproximam pré‑condições, pós‑condições e invariantes, permitindo refatorar com segurança desde que a semântica exigida permaneça preservada.

Exemplo: para uma função de ordenação, não basta verificar uma saída concreta; convém exigir que a saída seja ordenada, que seja uma permutação da entrada e que aplicar a função duas vezes produza o mesmo resultado (idempotência). Tais propriedades expressam o significado pretendido de forma concisa e resistente a mudanças internas de implementação.

## Casos de Uso

Projetar APIs e linguagens com regras claras sobre nulidade, exceções e concorrência; provar correção parcial/total de algoritmos críticos; validar equivalência após refatorações ou otimizações do compilador; e definir oráculos de [[Teste (Programação)]] a partir de especificações semânticas.

Em ambientes multiplataforma, usar a semântica para isolar variações de comportamento entre alvos (por exemplo, aritmética, horários, IO), garantindo que a lógica comum mantenha o mesmo significado enquanto adapta forma e bibliotecas às exigências locais.
