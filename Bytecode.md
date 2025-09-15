---
title: Bytecode
updated: 2025-09-15
---

## Definição

Bytecode é uma [[Representação (Software)|representação]] intermediária de programas, formada por instruções compactas destinadas à execução por uma máquina virtual. Situa‑se entre o código‑fonte e o código de máquina: é mais portátil que o binário nativo e mais próximo da execução que o texto original.

## Funcionalidade

É produzido por compiladores a partir do código‑fonte e consumido por máquinas virtuais que o interpretam ou o compilam just‑in‑time para código nativo. Essa camada permite portabilidade entre sistemas operacionais e arquiteturas, além de oferecer oportunidades de verificação de segurança, instrumentação e otimização em tempo de execução.

## Casos de uso

Ambientes amplamente adotados incluem o bytecode da [[JVM]] ([[Java]]/[[Kotlin]]), o DEX/ART no [[Android]] e o IL do .NET; muitas linguagens dinâmicas também geram bytecode interno (por exemplo, arquivos `.pyc` no Python). Em aplicações móveis e corporativas, o bytecode facilita distribuição multiplataforma e atualização de desempenho por JIT sem recompilar o aplicativo para cada arquitetura.

