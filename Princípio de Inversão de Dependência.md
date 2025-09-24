---
title: Princípio de Inversão de Dependência
updated: 2025-09-13
---
[[SOLID]]
## Definição

Dependências devem apontar para abstrações estáveis, não para detalhes voláteis. Políticas de alto nível controlam detalhes por contratos; implementações concretas encaixam‑se nesses contratos sem inverter a direção do acoplamento.

## Exemplo
Um serviço de faturamento depende de “RepositorioDePedidos” como contrato; implementações (SQL, memória, API externa) injetam‑se sem alterar o serviço. Testes substituem o repositório por dobras que respeitam o mesmo contrato.

## Cuidados e limites
Abstrações excessivas confundem e encarecem manutenção. A inversão funciona melhor quando interfaces capturam invariantes do domínio, não detalhes circunstanciais de tecnologia.

## Relações
[[SOLID]] · [[Teste Unitário]] · [[Desenvolvimento de Software]]

