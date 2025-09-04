---
title: Incerteza Residual
tags: [incerteza, entropia, informação]
created: 2025-09-04
updated: 2025-09-04
---
# Incerteza Residual

- “Quanto resta” de [[Incerteza]] sobre `Y` após conhecer `X`; formalmente, a [[Entropia Condicional]] `H(Y|X)`. É uma grandeza definida matematicamente (Shannon), independente do conceito de [[Ruído]]. No nível intuitivo, é a parte do estado de `Y` não capturada por correlações com `X` sob um [[Código]]/modelo.
- Em prática, corresponde ao erro previsível mínimo fora da amostra ao modelar `Y` a partir de `X` sob perda log; padrões “úteis” são os que reduzem essa incerteza sem inflar indevidamente a descrição do modelo (parcimônia/MDL), ver [[Aleatoriedade]].

## Interpretação (não definicional)
- Em engenharia de comunicação, essa incerteza residual é chamada de “[[Ruído]]” relativo a um [[Código]]/observador.

## Formalizações
- Shannon (discreto): `H(Y|X) = \sum_x p(x) H(Y|X=x) = H(X,Y) − H(X)`.
- Informação mútua: `I(X;Y) = H(Y) − H(Y|X) = H(X) − H(X|Y)`.
- Erro irredutível (regressão, perda quadrática): com `f*(x)=E[Y|X=x]`, vale `E[(Y−f*(X))^2] = E[Var(Y|X)]`. A variância condicional é a incerteza residual sob MSE.
- Perda log (classificação): `E[−log q(y|x)] = H(Y|X) + E_x KL(p(·|x) || q(·|x))`. O ótimo atinge `H(Y|X)`; fora do ótimo, o excesso é o desajuste do modelo.

## Intuições e exemplos
- Determinismo: se `Y=f(X)` sem ruído, então `H(Y|X)=0` (nenhuma incerteza residual).
- Independência: se `X ⟂ Y`, então `H(Y|X)=H(Y)` (saber `X` não ajuda).
- Canal binário simétrico (erro `p`): `H(Y|X)=H2(p)` — aumenta com o ruído do canal.
- Séries temporais: `H(X_{t+1} | X_{1:t})` mede o que o histórico ainda não explica; modelos melhores reduzem esse termo.

## Relações
- Conceitos: [[Entropia Condicional]] · [[Entropia Informacional]] · [[Aleatoriedade]] · [[Ruído]] · [[Shannon]] · [[Compressão de Informação]] · [[Código]].
- Canais: [[Transmissão de Informação]] · [[Canal e Fidelidade]] · [[Capacidade de Canal]].
- Aprendizado: generalização e MDL; reduzir `H(Y|X)` = aprender correlações reais. Overfitting não reduz a incerteza residual fora da amostra.

## Estimação prática
- Classificação: use perda log fora da amostra como estimativa para `H(Y|X)`; comparar com `H(Y)` informa o ganho de sinal `I(X;Y)`.
- Regressão: estime `E[Var(Y|X)]` aproximando `E[Y|X]` e medindo a variância dos resíduos; o platô com aumento de capacidade indica ruído irredutível.
- Não paramétrico: kNN/kernel para entropias/MI; cuidado com viés e dimensionalidade alta.

## Encadeamento conceitual
- Em [[Cosmologia Informacional]], quantifica o saldo de variação não codificado por um observador/código. Liga‑se à seta do [[Espaço-Tempo|tempo]] via crescimento de [[Entropia Informacional]] sob coarse‑graining fixo.

## Referências rápidas
- Shannon (1948); Slepian–Wolf (compressão com informação lateral); MacKay (Information Theory, Inference, and Learning Algorithms).
