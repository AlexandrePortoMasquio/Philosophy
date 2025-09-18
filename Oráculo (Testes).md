---
title: Oráculo (Software)
updated: 2025-09-16
---
Derivado de [[Software]] [[Oráculo (Software)]]

## Definição

Oráculo, em software, é o critério ou procedimento que decide, a partir de entradas e saídas observadas, se um comportamento está correto, de acordo com as finalidades determinadas por [[Requisito (Software)|requisitos]]. Torna verificáveis os requisitos ao transformar expectativas em regras de aceitação observáveis. Pode assumir a forma de resultados esperados, propriedades que devem sempre valer ou comparações com um comportamento de referência; relaciona-se diretamente a [[Precisificação]] e ao [[Contrato (Software)]].

## Funcionalidade

Concretiza critérios de aceitação de [[Teste (Software)]] em verificações objetivas: define quais entradas observar, quais saídas medir e como julgar (igualdade exata, tolerâncias numéricas, inclusão/ordem, ausência de efeitos colaterais). Em cenários com variância legítima, oráculos robustos aplicam normalizações e faixas de tolerância para evitar falsos positivos; quando resultados exatos são necessários, exigem igualdade determinística. A qualidade do oráculo depende de precisão, reprodutibilidade e relevância para o valor do sistema.

## Casos de Uso

Validação de APIs compara respostas ao contrato (campos obrigatórios, tipos e estados); cálculos numéricos usam tolerâncias definidas, não apenas igualdade bit a bit; verificações de formatação e ordenação aplicam normalizações antes do julgamento; suites de regressão utilizam oráculos de saída de referência (golden) ou de propriedades para impedir que alterações quebrem invariantes sem intenção. Ver também: [[Teste de Regressão]].

