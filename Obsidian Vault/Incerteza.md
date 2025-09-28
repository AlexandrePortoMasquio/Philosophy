---
title: Incerteza
tags: [incerteza, informação, probabilidade]
created: 2025-09-04
updated: 2025-09-04
---
# Incerteza

- Medida de imprevisibilidade de um estado/variável relativa a um código/modelo.
- TODO Como a incerteza e imprevisibilidade são relativas a um observador ou modelo, então essa noção NÃO é usada na [[Entropia Informacional]] [[Descentralismo|descentralista]].
- Na leitura informacional, quantifica-se por entropia de [[Shannon]] sob perda log (unidades em bits). Em geral, “incerteza” depende também da perda escolhida (ex.: MSE em regressão).

## Definições (Shannon)
- Entropia: `H(X) = − \sum_x p(x) \log p(x)` (discreto). Máxima quando `p` é uniforme no suporte finito; mínima (=0) quando `X` é determinístico.
- Regras: `H(X,Y) = H(X) + H(Y|X)` e `I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X)`.
- Contínuo: entropia diferencial `h(X)` pode ser negativa e não é invariante a reparametrização; prefira diferenças (ex.: `I`) e quantidades condicionais com cuidado.

## Tipos de incerteza
- Epistêmica: por limitação de modelo/dados; pode ser reduzida com informação adicional (condicionamento). Varia com o [[Código]]/observador.
- Intrínseca/aleatória: variabilidade que persiste mesmo no melhor modelo (ex.: ruído físico, estocasticidade); capturada por [[Incerteza Residual]] `H(Y|X)` quando `X` carrega toda a informação disponível.

## Relações úteis
- Incerteza residual: `H(Y|X)` mede o “quanto resta” sobre `Y` após `X` (ver [[Entropia Condicional]] e [[Incerteza Residual]]).
- Sinal vs ruído: `I(X;Y)` é a parte reduzida de incerteza ao conhecer `X`; o saldo é ruído relativo ao código (ver [[Ruído]] e [[Aleatoriedade]]).
- Compressão: fontes com menor `H` são mais compressíveis em média (limite de Shannon). Em objetos individuais, use [[Complexidade de Kolmogorov]]/[[Compressão de Informação]] como heurística de estrutura (padrões).

## Medidas sob outras perdas
- Regressão (MSE): incerteza preditiva irredutível = `E[Var(Y|X)]`. Divide-se heurísticamente em viés, variância do modelo e ruído dos dados.
- Classificação (perda log): risco ótimo fora da amostra = `H(Y|X)`; excesso = divergência `KL(p(·|x) || q(·|x))` do modelo.

## Estimação prática
- Discreto: estimador plug‑in (viés para amostras pequenas; correções tipo Miller–Madow).
- Contínuo: kNN/kernel/paramétricos; ou estimar perdas preditivas (log‑loss/MSE) como proxies consistentes.
- Cautelas: alta dimensionalidade, amostra pequena, discretização arbitrária e dependências temporais distorcem estimativas.

## Pitfalls
- Conflar entropia com “desordem” fora do contexto: aqui é medida de incerteza relativa a um modelo e uma perda (log‑loss).
- Usar `h(X)` como “incerteza absoluta” em contínuo; prefira informação mútua/diferenças.
- Confundir “parecer aleatório” com alta entropia: testes formais e compressão são guias, não provas universais.

## Ligações
- Conceitos: [[Shannon]] · [[Entropia Informacional]] · [[Entropia Condicional]] · [[Incerteza Residual]] · [[Aleatoriedade]] · [[Informação]] · [[Compressão de Informação]] · [[Complexidade de Kolmogorov]] · [[Código]].
- Sistemas e métodos: [[Transmissão]] · [[Canal e Fidelidade]] · [[Capacidade de Canal]] · [[Aprendizado de Máquina]] (generalização/risco) · [[Controle]].

