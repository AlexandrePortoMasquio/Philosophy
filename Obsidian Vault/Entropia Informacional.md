---
title: Entropia Informacional
tags: [entropia, informação]
created: 2025-08-28
updated: 2025-09-04
---
# Entropia Informacional

- Medida da dispersão/[[Aleatoriedade]] residual relativa a um código/modelo: quanto do estado não é capturado nem previsto (ruído) pelo código vigente.
- Une duas leituras complementares: [[Shannon]] (incerteza média H, entropia condicional H(·|·), informação mútua) e [[Complexidade de Kolmogorov]] (compressibilidade/descrição mínima de um objeto).
- Ordem informacional é o complementar: estrutura/compressibilidade e poder preditivo de um código; aprender reduz entropia condicional ao internalizar correlações (converter ruído em sinal).

## Formalizações (curtas)
- H(X): incerteza média de X; H(Y|X): incerteza residual de Y dado X (ruído relativo a X).
- I(X;Y): correlação útil entre X e Y; quanto maior, mais sinal/ordem informacional entre as variáveis.
- K(s): tamanho do menor programa que gera s; aproxima-se por [[Compressão]]; strings pouco compressíveis têm alta entropia algorítmica.
- Critério prático: MDL (descrição mínima) e erro preditivo out-of-sample — bons códigos minimizam ambos.

## Dinâmica e seta do tempo
- Em sistemas fechados, sob coarse-graining fixo, a entropia informacional tende a crescer (perda de distinções, irreversibilidade sob o código). A seta do tempo é o acúmulo de traços/seleções.
- Códigos que evoluem podem reduzir entropia local (capturando novas correlações), enquanto o saldo global de ruído relativo a códigos mais pobres pode aumentar.

## Encadeamento conceitual
- Fundamenta o [[Espaço-Tempo|tempo]]: a seta do tempo emerge do crescimento de entropia informacional (sob um recorte/código).
- [[Utilidade]] depende do tempo (decisão, processo, custo, oportunidade); portanto, utilidade não fundamenta entropia.

## Difere de entropia energética
- Não confundir com [[Entropia Energética]]: a energética trata da dispersão de energia sob leis termodinâmicas; a informacional mede incerteza/ruído relativo a um código. Em sistemas físicos, conectam-se via codificação de micro/macroestados.

## Medir na prática
- Estime distribuições para H/I; use compressores como proxy de K; monitore erro preditivo e robustez.
- Em [[Aprendizado de Máquina]], generalização é compressão útil (ordem); overfitting é pseudo-ordem que não reduz entropia fora do treino.

## Ligações
- Conecta [[Informação]] e processos de atualização em [[Virtualidade]].
- Importante para [[Descentralismo]] (feedbacks, ruído vs sinal).
- Relaciona-se a [[Compressão]] (ordem vs dispersão; redundância vs ruído).
- Relaciona [[Cosmologia Informacional]], [[Controle]] e [[Lei da Variedade Requisitada]].

## Fontes externas (referência)
- ../Articles/Drafts/Virtualidade e Informação - Da Virtualidade Deleuziana à Entropia Informacional.txt
