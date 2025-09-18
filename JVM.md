---
title: JVM
updated: 2025-09-16
---

## Definição

JVM (Java Virtual Machine) é um ambiente de execução portátil que carrega e executa programas compilados em [[Bytecode]] JVM, abstraindo detalhes de processador e sistema operacional. Fornece um modelo de memória, gerenciamento automático de memória ([[Coleta de Lixo (Software)]]) e verificação de segurança de código, permitindo que linguagens como [[Java]] e [[Kotlin]] executem sobre múltiplas plataformas sem recompilação nativa específica.

## Funcionalidade

O ciclo de execução envolve carregar classes, verificar bytecode (tipos, acessos, pilha), vincular dependências e interpretar ou compilar trechos quentes por JIT para melhorar desempenho. O coletor de lixo administra o heap, liberando objetos inacessíveis segundo estratégias que equilibram latência e throughput; o modelo de memória define garantias de visibilidade entre threads. A interface com o hospedeiro provê E/S, threads e bibliotecas padrão por meio de uma camada estável, enquanto a VM aplica otimizações dinâmicas guiadas por perfis reais de uso.

## Casos de Uso

Servidores e serviços de longa duração pela combinação de portabilidade, tooling maduro e desempenho competitivo; aplicações desktop e ferramentas que se beneficiam da mesma base; desenvolvimento [[Android]] por meio de bytecode JVM convertido para DEX. Em cenários de bibliotecas compartilhadas e produtos multiplataforma, a JVM atua como alvo comum que reduz custos de distribuição, enquanto o gerenciamento de [[Memória (Software)]] e o JIT simplificam a entrega de desempenho com segurança razoável.
