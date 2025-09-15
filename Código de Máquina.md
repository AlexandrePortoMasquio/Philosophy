---
title: Código de Máquina
updated: 2025-09-15
---

## Definição

Código de máquina é a sequência de instruções binárias executada diretamente por um processador, específica ao conjunto de instruções de uma arquitetura (por exemplo, x86‑64 ou ARM64). Difere do código‑fonte por não ser voltado à leitura humana, mas à execução fiel e eficiente pelo hardware.

## Funcionalidade

Controla operações do processador (cálculo, fluxo de controle, acesso à memória e a dispositivos) por meio de instruções codificadas em bits. É gerado, em geral, por compiladores ou montadores a partir de código de nível mais alto e é carregado pelo sistema operacional para execução. Otimizações em tempo de compilação e de linkagem ajustam o binário ao alvo para reduzir latência e consumo de recursos.

## Casos de uso

Sistemas operacionais, drivers, firmware e aplicações com requisitos estritos de desempenho e previsibilidade. Em ambientes embarcados, domina quando não há máquina virtual disponível; em desktops e servidores, compõe executáveis e bibliotecas nativas. Exemplos de destinos: ELF em Linux para x86‑64, Mach‑O em iOS para ARM64.

