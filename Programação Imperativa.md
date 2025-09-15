---
title: Programação Imperativa
updated: 2025-09-14
---

## Definição

A programação imperativa descreve sistemas como sequências de comandos que modificam estado e regulam o fluxo por meio de atribuições, condicionais e repetições. O foco recai no procedimento — como obter o resultado — e não apenas na relação entre entradas e saídas. Exemplo cotidiano: uma receita culinária define passos sucessivos que transformam ingredientes em um prato.

## Quais Áreas do Software Utilizam

Emprega-se amplamente no controle de [[Ciclo de Vida (Software)]] de aplicações e componentes, na orquestração de entrada/saída e comunicação de rede, na manipulação de arquivos e persistência, na automação de rotinas operacionais, em jogos e simulações, e em software embarcado. O traço comum é a necessidade de sequenciar ações com estado observável e tratar efeitos (tempo, falhas, dispositivos) em ordem definida.

## Aplicação em KMP

Em Kotlin Multiplatform (KMP), o estilo imperativo é apropriado nas bordas do sistema: ciclo de vida de aplicações, comunicação de rede, persistência e interação com dispositivos. No código compartilhado, convém limitar efeitos colaterais e concentrar mutações onde há necessidade operacional, preservando regras de negócio preferencialmente como transformações puras e estáveis.

## Implementação prática em KMP

Definir interfaces no `commonMain` para operações com efeitos (tempo, rede, persistência) e fornecer implementações específicas em `androidMain` e `iosMain`. Encapsular a mutação em componentes restritos (como repositórios ou controladores), expor funções suspensas que executam passos ordenados e tratar erros localmente, sem vazar detalhes ao domínio compartilhado. A interface de usuário por plataforma orquestra casos de uso e observa estados derivados, evitando dispersar lógica de negócio em manipuladores de eventos.

## Relações
[[Clean Architecture]] · [[Princípio de Responsabilidade Única]] · [[Kotlin]] · [[Multiparadigma]]
