---
title: Perfetto
tags: [android, desempenho, tracing]
created: 2025-09-15
updated: 2025-09-15
---

## Definição

Perfetto é uma ferramenta de rastreamento e análise de desempenho utilizada no [[Android]] (e também em Linux/[[Chrome]]) para registrar eventos do sistema e da aplicação em alta resolução temporal. Produz traços detalhados de CPU, GPU, memória, I/O, threads e marcações de app, permitindo identificar gargalos, jank, travamentos e contenções com precisão. Os traços podem ser capturados no dispositivo e inspecionados em uma interface visual baseada em navegador.

## Funcionalidade

O fluxo básico envolve habilitar categorias de eventos, iniciar a captura, reproduzir o cenário alvo (por exemplo, rolagem de lista ou carregamento de tela) e encerrar a sessão para analisar o traço. A visualização apresenta trilhas por processo/thread, schedulers e marcações customizadas da aplicação. A correlação entre picos de uso de CPU, pausas de GC e frames perdidos revela o ponto de estrangulamento. Anotações (slices) inseridas pelo app permitem delimitar trechos críticos e medir durações fim‑a‑fim.

## Casos de Uso

Diagnóstico de quedas de frame (jank) em [[Lista (Software)|listas]] e animações; investigação de latência em requisições e desserialização; identificação de contenção de locks e excesso de trabalho no main thread; análise de regressões entre versões. Exemplo cotidiano: uma tela “engasga” ao abrir; o traço mostra trabalho pesado de parsing no main thread coincidindo com perda de frames — a solução desloca o parsing para uma thread de fundo e reduz alocação.

## Em KMP

Em projetos [[KMP]], a instrumentação que aparece no Perfetto é específica do Android; por isso, recomenda‑se encapsular o tracing no módulo compartilhado como um contrato simples (interface) e fornecer implementações por plataforma (expect/actual). No Android, a implementação usa o mecanismo de trace do sistema para que as marcações fiquem visíveis no Perfetto; no iOS, pode redirecionar para signposts do Instruments ou, na ausência de necessidade, operar como no‑op. Assim, casos de uso e repositórios podem marcar trechos críticos sem acoplar o domínio à plataforma.

Anotar operações com início/fim estáveis: chamadas de rede, serialização/desserialização, mapeamentos, consultas ao cache e transações de banco. As marcações de UI e frames devem permanecer no app Android (Compose), delimitando eventos que impactam fluidez (carregamento de tela, listas pesadas). Para evitar sobrecarga em produção, habilitar o tracing por flag de diagnóstico e limitar categorias ao escopo da investigação.
