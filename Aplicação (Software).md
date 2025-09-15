---
title: Aplicação (Software)
updated: 2025-09-14
---

## Definição

Em [[Software]], uma aplicação é um [[Programa]] orientado a um objetivo definido que oferece capacidades em um contexto de uso por meio de [[Interface|interfaces]] e coordena recursos de computação ([[Processamento (Software)]], [[Memória (Software)]], armazenamento e rede). Caracteriza-se por um conjunto de funcionalidades coesas, regras de operação e limites claros de responsabilidade e integração com o ambiente de execução.

## Aplicação em KMP

Em Kotlin Multiplatform (KMP), a aplicação organiza-se separando o núcleo de domínio no `commonMain` de detalhes específicos de plataforma em `androidMain` e `iosMain`. O domínio expõe casos de uso e modelos estáveis; serviços voláteis (tempo, rede, persistência) são acessados por meio de contratos definidos no código comum e implementados por plataforma, permitindo evolução local sem afetar as regras centrais.

## Boas práticas em KMP

Delimitar fronteiras por responsabilidade, aplicar inversão de dependência no acesso a serviços, evitar lógica de negócio na interface de usuário e tratar ciclo de vida e persistência nas bordas. Preferir funções puras no domínio, uso parcimonioso de mutação e testes em `commonTest` cobrindo regras essenciais; nas plataformas, restringir-se à orquestração, ao mapeamento de dados e à adaptação a APIs do sistema, preservando coesão e clareza.
