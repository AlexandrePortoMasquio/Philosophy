---
title: Endereçamento (Software)
updated: 2025-09-15
---

## Definição

Endereçamento, em software, é o modo pelo qual programas referem posições em um espaço de endereços para ler e escrever dados ou aceder a código. No nível de execução, cada processo opera sobre endereços lógicos/virtuais que o [[Kernel (Software)]] mapeia para memória física por meio de tabelas e políticas de proteção. O esquema pode ser absoluto (um endereço fixo), relativo (deslocamento a partir de um ponto) ou simbólico (nomes resolvidos pelo carregador). Diferencia‑se de endereçamento de rede, que identifica nós e serviços; aqui, trata‑se de localizar conteúdo em [[Memória (Software)]].

## Funcionalidade

Carregadores resolvem símbolos e aplicam realocação; a unidade de gerenciamento costuma ser a página, que permite isolamento, paginação sob demanda e execução apenas‑leitura ou não‑executável. Técnicas como ASLR embaralham a disposição para mitigar exploração. Em linguagens com ponteiros e referências, o modelo de endereçamento condiciona segurança e desempenho: aritmética de ponteiros pode corromper estado; referências seguras delegam a checagens do runtime e à coleta de lixo. Em 32 bits, o espaço virtual limita o teto de memória endereçável; em 64 bits, a ampliação reduz colisões, mas não elimina a necessidade de layout atento e localidade.

## Casos de Uso

Bibliotecas dinâmicas dependem de realocação e resolução de símbolos para compartilhar código entre processos. Mapeamentos de arquivo em memória (memory‑mapped files) expõem conteúdo persistente como regiões endereçáveis, úteis para processamento eficiente de grandes volumes. Em aplicações gráficas e móveis, organização de estruturas no espaço de endereços afeta latência: dispor dados de acesso contíguo reduz falhas de cache e melhora fluidez. Exemplos cotidianos: um executável “portátil” que roda em diferentes máquinas graças a endereçamento relativo; um aplicativo de fotos que evita carregamentos desnecessários mantendo apenas miniaturas mapeadas.

