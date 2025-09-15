---
title: Princípio de Substituição de Liskov
updated: 2025-09-13
---

## Definição

O princípio de substituição de Liskov afirma que tipos derivados devem poder substituir seus básicos sem violar promessas observáveis. Pré‑condições não podem ser fortalecidas, e pós‑condições e invariantes não podem ser afrouxados de modo a quebrar usos válidos previstos pelo contrato.

## Exemplo
Se “Pagamento” promete lançar exceções específicas e registrar auditoria, implementações derivadas devem manter essas garantias. Acrescentar requisitos extras de estado ou suprimir registros viola a substituibilidade.

## Cuidados e limites
Herdar sem contrato claro induz violações sutis. Em muitos casos, composição e contratos específicos são preferíveis à herança para preservar substituibilidade sem hierarquias frágeis.

## Relações
[[SOLID]] · [[Testes Unitários]]

