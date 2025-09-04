---
title: Entropia Condicional
tags: [entropia, shannon, informação]
created: 2025-09-04
updated: 2025-09-04
---
# Entropia Condicional

- [[Incerteza residual]] de `Y` dado `X`: quanto do estado de `Y` não é capturado pelas correlações com `X` (ruído relativo a `X`) sob um código/modelo. Central para [[Shannon]] e para a leitura de [[Entropia Informacional]].

## Definição (discreta)
- `H(Y|X) = Σ_x p(x) H(Y|X=x) = H(X,Y) − H(X)`.
- Relação com informação mútua: `I(X;Y) = H(Y) − H(Y|X) = H(X) − H(X|Y)`.
- Intuição: é o “quanto ainda falta” saber sobre `Y` depois de conhecer `X`.

## Definição (contínua)
- Entropia diferencial: `h(Y|X) = h(X,Y) − h(X)`.
- Observações: `h(·)` pode ser negativa e depende de reparametrizações; diferenças que definem `I(X;Y)` permanecem bem definidas. Use com cuidado ao comparar valores absolutos.

## Intuições e exemplos
- Função sem ruído: se `Y = f(X)` determinística, então `H(Y|X) = 0`.
- Independência: se `X ⟂ Y`, então `H(Y|X) = H(Y)`.
- Canal binário simétrico (BSC) com prob. de erro `p`: `H(Y|X) = H2(p)` (entropia binária). Quanto maior o ruído do canal, maior a entropia condicional.

## Propriedades
- Cadeia: `H(X1,…,Xn) = Σ_i H(Xi | X1,…,X_{i−1})`.
- Monotonicidade: condicionar não aumenta entropia — `H(Y|X,Z) ≤ H(Y|X)`.
- Assimetria: em geral `H(X|Y) ≠ H(Y|X)`.
- Limites: `0 ≤ H(Y|X) ≤ H(Y)` (discreto). Igualdades nos casos determinístico e independente.
- Processamento reduz informação: se `Z = g(X)`, então `H(Y|Z) ≥ H(Y|X)` (equivalente a `I(Y;Z) ≤ I(Y;X)`).

## Relações com compressão e predição
- Fonte com informação lateral: `H(Y|X)` é a taxa mínima adicional média para codificar `Y` conhecendo-se `X` (limite de Slepian–Wolf em compressão distribuída).
- Perda log (classificação): a perda log ótima fora da amostra iguala `H(Y|X)`. Decomposição: `E[-log q(y|x)] = H(Y|X) + E_x KL(p(·|x) || q(·|x))`. Logo, um bom modelo `q` aproxima `H(Y|X)`; reduzir `H(Y|X)` = aprender correlações úteis.
- MDL/Parcimônia: padrões “úteis” são os que reduzem `H(Y|X)` e a descrição total (modelo + resíduos) sem overfitting.

## Em canais (Shannon)
- `H(Y|X)`: ruído do canal (incerteza na saída dado o símbolo enviado).
- `H(X|Y)`: equívoco (incerteza sobre o símbolo enviado dado o recebido).
- Capacidade: `C = max_{p(x)} I(X;Y) = max_{p(x)} [H(Y) − H(Y|X)]`. Para um canal fixo `p(y|x)`, `H(Y|X)` depende de `p(x)` via média sobre `x`.

## Estimação prática
- Discreto: estimador plug‑in a partir de contagens (viés finito; considerar correções como Miller–Madow).
- Contínuo: estimadores kNN/paramétricos; alternativamente, modelar `p(y|x)` e medir perda log fora da amostra como proxy de `H(Y|X)`.
- Aproximar `I(X;Y)`: estime `H(Y)` pelos rótulos e subtraia a perda log out‑of‑sample do melhor modelo disponível.

## Ligações
- Conceitos: [[Shannon]] · [[Entropia Informacional]] · [[Informação]] · [[Compressão de Informação]] · [[Código]] · [[Ruído]] · [[Aleatoriedade]].
- Relacionados: Informação Mútua (I) · Regra da cadeia · Limite de Slepian–Wolf · [[Transmissão de Informação]] · [[Canal e Fidelidade]].

## Referências rápidas
- Shannon (1948): A Mathematical Theory of Communication.
- Cobertura moderna: NIST, MacKay (Information Theory, Inference, and Learning Algorithms).

