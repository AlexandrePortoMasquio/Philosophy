---
title: Código de Alvo
updated: 2025-09-21
---
[[API de Destino]]
## Definição

Código de alvo é o artefato gerado por um compilador ou tradutor para uma plataforma específica: instruções executáveis ou representações intermediárias adequadas ao destino (por exemplo, [[Bytecode]] para [[JVM]], binários nativos, módulos JavaScript). Distingue‑se de [[Código-Fonte]] por já incorporar decisões sobre conjunto de instruções, chamada de funções, layout de dados e convenções da plataforma.

## Funcionalidade

A forma do código de alvo depende do back‑end e do ambiente de execução. Para [[JVM]]/[[Android]], produz‑se [[Bytecode]] que depois pode ser transformado em [[DEX (Programação)]]; para nativo, emite‑se [[Código Máquina]]/ligações via toolchain do sistema; para web, gera‑se JavaScript alinhado ao módulo escolhido. Metadados, símbolos e informações de tipos podem acompanhar o artefato para depuração, interoperabilidade e otimizações.

O processo de geração aplica convenções do alvo (ABI, chamadas, alocação de registradores), insere prólogo/epílogo de funções, realiza otimizações seguras no nível do destino e organiza seções do binário conforme o carregador do sistema. Quando há mais de um alvo, a base comum é recompilada para cada um, preservando a semântica e adaptando forma e desempenho locais.

## Casos de Uso

Distribuir bibliotecas em múltiplos formatos: JAR/AAR para o ecossistema JVM/Android, frameworks para iOS/Native, pacotes npm para JavaScript. Em projetos multiplataforma, compilar o mesmo módulo para diferentes alvos permite compartilhar domínio e regras de negócio, enquanto UI e interop respeitam as particularidades de cada ambiente. Em otimização, analisar o código de alvo (desassemblar, inspecionar mapas de símbolos) guia ajustes de desempenho e tamanho do binário.

