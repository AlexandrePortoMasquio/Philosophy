---
title: Coleta de Lixo (KMP)
updated: 2025-09-16
---
Derivado de [[KMP]]

## Definição

Em [[KMP]] (Kotlin Multiplatform), “coleta de lixo” refere‑se aos mecanismos de gerenciamento de [[Memória (Software)]] presentes nos diferentes alvos (JVM/[[Android]], JavaScript, Native/iOS) e às implicações desse pluralismo para o desenho de APIs e dados compartilhados. Não há um único coletor global: cada runtime gerencia seu heap conforme suas regras; o objetivo é compor essas diferenças com contratos claros e fronteiras de dados estáveis.

## Funcionalidade

No alvo JVM/ART (Android), vale a [[Coleta de Lixo (Android)]] com GC geracional/concorrente; no JavaScript, a VM do navegador/engine aplica GC próprio; no Native (Kotlin/Native), o gerenciamento combina estratégias do runtime (memória segura moderna) e integração com ARC no lado iOS/Swift. Como não existe GC compartilhado entre processos/runtimes, atravessar fronteiras pode implicar cópias e retenções distintas; grafos grandes e mutáveis amplificam custos.

Boas práticas: modelar dados imutáveis no módulo comum; limitar o tamanho de objetos atravessando fronteiras; serializar apenas o necessário; e projetar APIs que evitem ciclos de referência. Em integrações Android↔shared e iOS↔shared, preferir conversões explícitas nas bordas e perfilar alocação/pausas com ferramentas da plataforma (por exemplo, [[Perfetto]] e Instruments) antes de otimizar.

## Casos de Uso

Aplicativos que compartilham domínio/dados entre Android e iOS: reduzir interop de objetos muito aninhados e padronizar formatos de transferência melhora latência e uso de memória. Exemplo cotidiano: telas de lista consomem modelos leves do shared; conversões para modelos de UI ocorrem localmente em cada plataforma, evitando transportar estruturas pesadas pela ponte.

