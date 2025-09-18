---
title: Endereço de Memória
updated: 2025-09-16
---
Derivado de [[Memória (Software)]]

## Definição

Endereço de memória é o identificador de uma posição no espaço de endereços de um processo ou sistema, usado para localizar código e [[Dados (Software)]]. Distingue‑se o endereço virtual (visível ao programa) do físico (linhas reais de RAM); o mapeamento entre ambos é mediado pelo [[Kernel (Software)]] e pela MMU. Faz parte de [[Endereçamento (Software)]]: além do valor do endereço, importam a unidade de endereçamento (byte, palavra), alinhamento e as fronteiras de acesso válidas.

## Funcionalidade

Em sistemas modernos, programas manipulam endereços virtuais; a tradução para físico ocorre por tabelas de páginas, com proteção (leitura/escrita/execução) e isolamento entre processos. Linguagens com [[Ponteiro (Software)|ponteiros]] expõem endereços diretamente; linguagens com referências abstraem o detalhe, mas continuam a depender de endereços válidos. A aritmética de endereços deve respeitar limites de região (pilha, heap, áreas mapeadas; ver [[Espaço (Memória)]]) e alinhamento, sob pena de falhas (violação de segmentação) ou desempenho inferior por perdas de localidade.

## Casos de Uso

Mapeamento de arquivos (memory‑mapped files) expõe conteúdo persistente como regiões contíguas endereçáveis; acesso sequencial contíiguo favorece prefetch e cache. Estruturas como vetores/arrays exploram endereços contíguos para acesso por índice; listas encadeadas trocam contiguidade por flexibilidade. Exemplo cotidiano: um programa que tenta ler além do tamanho de um vetor incorre em acesso a endereço inválido e é finalizado pelo sistema; ao manter acessos dentro de limites e dados contíguos, reduz‑se latência e melhora‑se a previsibilidade.

