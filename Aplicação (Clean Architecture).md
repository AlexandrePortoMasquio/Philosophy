---
title: Aplicação (Clean Architecture)
updated: 2025-09-22
---
Derivado de: [[Clean Architecture]]
Relacionado a: [[Aplicação (Programação)|Aplicação (Software)]] · [[UseCase]] · [[Port|Porta]]

## Definição

A camada de Aplicação, em Clean Architecture, define e executa [[UseCase]]s do sistema. Orquestra a interação entre as regras do [[Domínio (Clean Architecture)]] e as bordas por meio de portas, estabelecendo a sequência das ações, limites transacionais e políticas de orquestração. Não depende de interface, banco de dados ou rede; expressa o que deve acontecer e em que ordem, preservando a independência das regras centrais.

## Funcionalidade

Valida entradas e pré‑condições, convoca entidades e serviços do domínio, controla transações (início, confirmação, cancelamento) e traduz erros em resultados claros do domínio. Opera sem estado próprio e com contratos de entrada e saída definidos por tipos estáveis, mantendo coesão e previsibilidade. Decide o “o quê” e o “quando” da ação, deixando “como” persistir ou apresentar às camadas externas.

## Casos de Uso

Exemplos típicos incluem “efetuar login”, “criar pedido” ou “atualizar perfil”: cada operação reúne validações, consultas e gravações necessárias por meio de portas, devolvendo um resultado único e verificável. Em aplicações móveis (KMP/Android), a [[ViewModel]] invoca esses casos de uso, enquanto repositórios e gateways são injetados na Aplicação; a substituição de infraestrutura (p.ex., cliente HTTP ou armazenamento) não altera a lógica aqui definida, o que favorece testabilidade e evolução independente.

