---
title: DEX (Programação)
updated: 2025-09-21
---
[[Compilação (Programação)]], [[Código de Alvo]]
## Definição

DEX (Dalvik Executable) é o formato de bytecode usado em [[Android]] para representar programas em nível de máquina virtual. Reúne classes, métodos, campos e constantes em uma estrutura única, com instruções baseadas em registradores (em contraste com o modelo em pilha da [[JVM]]). O arquivo `.dex` torna‑se o código de alvo do aplicativo, normalmente empacotado como `classes.dex` dentro do APK/AAB, acompanhado de tabelas de tipos, strings e informações de depuração.

## Funcionalidade

O código‑fonte (por exemplo, Java/Kotlin) é transformado em bytecode de classes e, em seguida, convertido para DEX pelo toolchain do Android (etapas de “dexing” e, quando aplicável, redução/otimização). Em execução, a runtime do Android interpreta ou compila adiantado/just‑in‑time o DEX para código nativo conforme a versão e as políticas do sistema, preservando semântica e aplicando otimizações seguras.

O formato DEX deduplica referências (strings, tipos, métodos) para reduzir tamanho e melhora o carregamento em dispositivos móveis. Cada arquivo possui limites práticos, como o número máximo de referências a métodos, o que motiva particionamento em múltiplos arquivos (multidex) em projetos extensos. Ferramentas de inspeção permitem verificar tabelas, instruções e símbolos para diagnóstico e depuração.

## Casos de Uso

Construção de aplicativos Android: bibliotecas e apps publicam e consomem artefatos que incluem DEX como código executável. Em otimização, analisar o `.dex` auxilia a reduzir tamanho do aplicativo e inicialização, identificando classes e métodos redundantes. Em projetos grandes, configurar multidex e monitorar o limite de referências evita falhas de build e problemas de carregamento.

Relação com multiplataforma: ao direcionar o alvo Android em projetos comuns, o DEX é o formato final de execução local, integrando‑se com a base compartilhada e com APIs específicas da plataforma, mantendo fronteiras claras entre o código comum e o específico.

