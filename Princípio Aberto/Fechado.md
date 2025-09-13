---
title: Princípio Aberto/Fechado
updated: 2025-09-13
---

Módulos devem ser abertos à extensão e fechados à modificação de seu núcleo estável. A extensão ocorre por composição ou herança controlada, preservando contratos e isolando variações.

## Exemplo
Regras de cálculo configuráveis por estratégia evitam editar o núcleo do faturamento ao acrescentar um novo tributo. A extensão entra por um ponto de variação explícito, mantendo o contrato existente.

## Cuidados e limites
Extensibilidade prematura produz indireções supérfluas. O fechamento depende de identificar o que é realmente estável; contratos imprecisos convidam à modificação do núcleo.

## Relações
[[SOLID]] · [[Desenvolvimento de Software]] · [[Precisificação]]

