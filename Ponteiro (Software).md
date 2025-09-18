---
title: Ponteiro (Software)
updated: 2025-09-16
---
Derivado de [[Memória (Software)]]

## Definição

Ponteiro é um [[Valor (Programação)]] que é acessível por um [[Endereço de Memória]] e permite acessar indiretamente algum [[Código]] ou [[Dados (Software)]]. Em linguagens que o expõem diretamente (como C/C++), admite operações como obtenção de endereço, desreferência e aritmética (avançar/retroceder posições). Distingue‑se de referências opacas (geridas por runtime/GC) por exigir do programa a garantia de validade, alinhamento e limites do alvo; um ponteiro nulo, pendente ou fora de faixa viola o contrato de acesso.

## Funcionalidade

O uso correto de ponteiros envolve: estabelecer a origem lícita do endereço (alocação, objeto estático ou mapeamento), respeitar o tipo/alinhamento, evitar ultrapassar fronteiras de regiões (pilha, heap, mapeados; ver [[Espaço (Memória)]]) e coordenar vida útil (criação/liberação) para impedir uso‑após‑liberação ou dupla liberação. Aritmética de ponteiros pressupõe contiguidade e tamanho do elemento; aliasing (vários ponteiros para a mesma região) requer disciplina para evitar condições de corrida e efeitos inesperados. Em plataformas com MMU, acessos inválidos resultam em falhas; em ambientes com verificação mais fraca, geram corrupção silenciosa difícil de diagnosticar.

## Casos de Uso

Programação de baixo nível: sistemas operacionais, drivers e acesso a memória mapeada de dispositivos; bibliotecas de alto desempenho que percorrem buffers contíguos (imagens, áudio, redes); interoperabilidade (FFI) entre linguagens e chamadas a APIs nativas. Exemplo cotidiano: processar uma imagem iterando por linhas com deslocamentos (stride); ao respeitar limites e alinhamento, evita‑se leitura/escrita fora de faixa e preserva‑se a previsibilidade do desempenho.

