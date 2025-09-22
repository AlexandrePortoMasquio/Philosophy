---
title: MVVM
updated: 2025-09-22
---
[[Arquitetura KMP]], [[Arquitetura Android]], [[Arquitetura de Software]]
## Definição

MVVM ([[Model (MVVM)|Model]]–[[Interface de Usuário|View]]–[[ViewModel]]) é um padrão de apresentação que separa a interface de usuário do [[Estado (MVVM)]] e da lógica que a alimenta. A View exibe dados e encaminha eventos; a ViewModel expõe estado legível e comandos, coordena casos de uso e não conhece widgets concretos; o Model reúne regras de domínio e acesso a dados. O objetivo é reduzir acoplamento entre UI e regras, facilitar testes e permitir evolução independente das partes.

## Funcionalidade

O fluxo é, em geral, unidirecional: a View observa estado exposto pelo ViewModel e envia intenções ([[Evento (MVVM)|eventos]]) que o ViewModel traduz em ações sobre o domínio. A ViewModel transforma resultados do [[Domínio (MVVM)]] em estados de tela (carregando, conteúdo, erro) e emite efeitos de curto prazo (navegação, mensagens) de modo controlado. Em contextos multiplataforma, a lógica de domínio permanece no módulo comum, e a camada de apresentação pode expor fluxos observáveis adequados a cada plataforma, preservando contratos e mantendo a UI nativa.

## Casos de Uso

Aplicativos móveis com telas dirigidas por estado: a ViewModel mapeia consultas e comandos do domínio para estados imutáveis apresentados pela UI. Benefícios incluem testes do estado e dos encadeamentos sem dependência de UI, clareza na modelagem de erros e simplificação de mudanças na camada de apresentação. Em projetos KMP, compartilha‑se o domínio e, quando conveniente, um adaptador de apresentação que fornece fluxos para Android e iOS, mantendo componentes visuais específicos em cada plataforma.

