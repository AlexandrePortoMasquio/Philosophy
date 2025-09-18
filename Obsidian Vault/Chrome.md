---
title: Chrome
tags: [navegador, web, software]
created: 2025-09-15
updated: 2025-09-15
---

## Definição

Chrome é um navegador web multiplataforma baseado no projeto Chromium, com motor de renderização Blink e motor JavaScript V8. Fornece um ambiente de execução para aplicações web, suporte a padrões modernos, isolamento por processos e ferramentas integradas para desenvolvimento e diagnóstico. Está disponível em [[Linux]], Windows, macOS, [[Android]] e iOS, com sincronização opcional de dados entre dispositivos.

## Funcionalidade

Oferece navegação por abas, perfis, modo anônimo, gerenciamento de permissões e extensões. As Ferramentas do Desenvolvedor (DevTools) permitem inspecionar DOM/CSS, monitorar rede, medir desempenho (Performance), memória (Memory), layout e pintura (Rendering), além de registrar rastros. Em plataformas suportadas, integra‑se a mecanismos de tracing de baixo nível; no ecossistema Android e Linux, pode produzir e analisar traços por meio do [[Perfetto]].

## Casos de Uso

Desenvolvimento e depuração de aplicações web (inspeção de rede, layout, eventos e métricas de performance); análise de jank em rolagem/animações com a aba Performance; investigação de vazamentos de memória com perfis de heap; diagnóstico de regressões de tempo de carregamento entre versões. Exemplo cotidiano: uma página “engasga” ao rolar; a captura de desempenho revela scripts longos bloqueando o thread principal e layout thrashing — a correção reduz trabalho síncrono e agrupa leituras/escritas de layout.

