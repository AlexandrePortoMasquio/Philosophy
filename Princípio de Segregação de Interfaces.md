---
title: Princípio de Segregação de Interfaces
updated: 2025-09-13
---

Evitar interfaces inchadas: consumidores não devem depender de métodos que não usam. Contratos pequenos e específicos reduzem dependências e permitem implementações focadas.

## Exemplo
Separar “LeituraDeRelatorio” de “EscritaDeRelatorio” evita que clientes de leitura precisem fornecer capacidades de escrita ou tratar erros que não lhes dizem respeito.

## Cuidados e limites
Fragmentação excessiva torna a composição custosa. A segregação deve seguir fluxos reais de uso e pontos de estabilidade do domínio.

## Relações
[[SOLID]] · [[Desenvolvimento de Software]] · [[Software]]

