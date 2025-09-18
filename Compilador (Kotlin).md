---
title: Compilador (Kotlin)
updated: 2025-09-16
---
Derivado de [[Kotlin]]

## Definição

O compilador do Kotlin transforma código‑fonte em artefatos executáveis para múltiplos alvos: [[Bytecode]] de [[JVM]] (usado também em [[Android]]), JavaScript e binários nativos. O front‑end realiza análise léxica e sintática, resolução de tipos e checagens de segurança (por exemplo, nulidade); a representação intermediária unifica a geração para back‑ends distintos. A geração K2 substitui gradualmente a anterior, buscando consistência entre plataformas e melhor desempenho de análise.

## Funcionalidade

No destino JVM, o compilador produz classes e metadados compatíveis com o ecossistema Java, permitindo interoperabilidade direta com [[Java]]; no Android, esse bytecode é posteriormente convertido para DEX pelo toolchain da plataforma. No destino JS (IR), gera código JavaScript moderno e módulos; no destino Native, compila para binários via LLVM, sem máquina virtual. Em projetos [[KMP]], o compilador organiza source sets (common/targets) e aplica `expect/actual` para conciliar APIs específicas com código comum.

O pipeline admite incrementalidade e plugins (por exemplo, processadores de anotação/símbolos), reporta avisos/erros com posições precisas e aplica otimizações adequadas ao alvo. A emissão de metadados preserva informações de tipos e nulidade para chamada cruzada entre linguagens e módulos, favorecendo segurança e manutenção.

## Casos de Uso

Aplicações Android e servidores na JVM compilam o mesmo código Kotlin com perfis distintos de otimização e empacotamento; bibliotecas multiplataforma publicam artefatos para JVM/JS/Native a partir de uma base comum; aplicações iOS consomem binários de Kotlin/Native gerados do módulo compartilhado. Em todos os cenários, o ajuste de alvos, níveis de linguagem e warnings do compilador contribui para estabilidade, desempenho e clareza de contrato.

