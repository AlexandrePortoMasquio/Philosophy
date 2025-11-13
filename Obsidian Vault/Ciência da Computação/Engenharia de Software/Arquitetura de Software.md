---
title: Arquitetura de Software
tags: [engenharia de software, arquitetura]
created: 2025-08-28
updated: 2025-08-28
---
[[Programação]] ······················
## Ideia
- Arquitetura é a organização intencional de componentes e relações para satisfazer requisitos funcionais e não funcionais sob restrições.
- Conecta teoria e prática: estrutura (formas), níveis (granularidade) e mecanismos de controle (fluxo, estado, isolamento) direcionam decisões.

## Qualidades Arquiteturais
- Desempenho, escalabilidade, confiabilidade, segurança, manutenibilidade, evolutividade, portabilidade.
- Trade-offs explícitos: escolhas de estilo (camadas, [[Microsserviço|microsserviços]], monólito modular, event-driven) influenciam custos e capacidades.

## Estilos e Decisões
- Camadas: separação de responsabilidades; facilita substituição e testes.
- Monólito Modular: limites internos nítidos com compilação/implantação unificada.
- Microsserviços: autonomia e implantação independente; custo e [[Sistemas Distribuídos|distribuição]].
- Event-Driven: acoplamento fraco temporal; aumenta latência e complexidade de rastreio.

## Prática
- Documentar decisões (ADRs) com contexto, alternativas e consequências.
- Medir: perfis de latência, budget de erros, limites de throughput.
- Evoluir com experimentos controlados (feature flags, canary) e revisões arquiteturais periódicas.

## Ligações
- [[Modularidade]] , [[Padrões de Projeto]] (aplicação local), [[Processos]] (governança), [[Ferramentas]] (observabilidade, automação).
- [[Engenharia de Software Mobile/Engenharia de Software Mobile|Mobile]] (camadas, limites, sincronização offline), [[Banco de Dados]] (modelagem), [[Sistemas Distribuídos]] (consistência/replicação).
