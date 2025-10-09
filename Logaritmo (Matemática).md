---
title: Log (Matemática)
updated: 2025-09-29
---
[[Matemática]]
## Definição

Um log, ou logaritmo, é uma operação matemática inversa da exponenciação, que representa o expoente a que uma base deve ser elevada para resultar em um determinado número (o logaritmando).

O logaritmo de base b>0, b≠1, de um número a>0 é o expoente x tal que b^x = a: escreve-se log_b a = x. Trata-se da função inversa da exponenciação em base b. O logaritmo natural adota a base e e geralmente se denota por ln a.

Em termos práticos, mede quantas multiplicações por um mesmo fator são necessárias para alcançar um valor. Exemplo cotidiano: o número de dígitos de um inteiro positivo em base 10 é ⌊log_10 n⌋ + 1; dividir repetidamente um conjunto ao meio para localizar um elemento (busca binária) requer cerca de log_2 n etapas.

## Derivação

As propriedades decorrem da [[Lei dos Expoentes]]: b^x·b^y = b^{x+y} implica log_b(xy) = log_b x + log_b y; (b^x)^k = b^{kx} implica log_b(x^k) = k·log_b x; e, de b^x = a e c^y = a, resulta a mudança de base log_b a = (log_c a)/(log_c b). Para b>1, a função x ↦ log_b x é crescente, contínua e côncava em (0, ∞); para 0<b<1, é decrescente.

Na modelagem de processos multiplicativos por etapas constantes (crescimento ou decaimento proporcional), o tempo para atingir um nível obedece a uma lei logarítmica. Essa inversão converte escalas multiplicativas em aditivas, simplificando comparações e a soma de efeitos repetidos.

## Relações

O logaritmo relaciona-se diretamente à [[Potência]] como sua inversa e organiza fenômenos por ordens de grandeza: diferenças iguais em escala logarítmica correspondem a razões iguais em escala linear. Em análise de algoritmos, aparece na classificação assintótica, como em [[Notação Big O]], indicando custos que crescem lentamente com o tamanho da entrada.

Cuidados: a base especifica a unidade de medida; omissões podem induzir erro (bases 2, 10 e e têm interpretações distintas). A função admite apenas argumentos positivos; aplicações físicas exigem grandezas definidas e não nulas. “Crescimento logarítmico” descreve aumento lento, mas não nulo; pode ser irrelevante para entradas pequenas e decisivo em regimes de grande escala.

