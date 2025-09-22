---
title: Plataforma (Programação)
updated: 2025-09-21
---
Derivado de [[Programação]]

## Definição

Plataforma, em programação, é o ambiente que sustenta a execução de programas e oferece serviços estáveis: combinação de hardware, sistema, runtime e bibliotecas com regras, versões e distribuição próprias. Define o que está disponível para uso (APIs, convenções), como o código é empacotado e executado, e quais garantias e limites estruturam o comportamento. Em projetos, a plataforma orienta escolhas de alvo, compatibilidade e publicação (ver [[API de Destino]] e [[Compilação (Programação)]]).

## Funcionalidade

Uma plataforma determina contratos técnicos: modelos de memória e de concorrência, tratamento de erros, formatos de artefato e políticas de segurança. Em desenvolvimento, filtra chamadas com base em versões de API, guia a compilação e vinculação, e regula a interação com recursos do sistema. Em execução, provê ciclo de vida, isolamento e serviços (tempo, rede, armazenamento), além de supervisionar permissões e consumo de recursos. O [[Código de Alvo]] resulta adaptado a essas convenções para manter correção e desempenho.

## Casos de Uso

Escolher plataforma conforme requisitos de produto (alcance de dispositivos, capacidades nativas, distribuição). Projetar camadas que separem lógica comum de integrações específicas, reduzindo custo de manutenção e facilitando testes. Em migração ou multiplataforma, mapear diferenças de API e de comportamento observável e ajustar pontos de variação explícitos, preservando o significado do programa e a compatibilidade com usuários e ecossistemas.

