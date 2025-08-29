---
title: Banco de Dados
tags: [engenharia de software, banco de dados]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Sistema para armazenar, consultar e proteger estado persistente. Escolhas impactam consistência, desempenho e evolução.

## Modelos
- Relacional (SQL): tabelas, chaves, restrições; forte consistência e [[Álgebra Relacional]].
- Documento, chave-valor, coluna larga, grafo: flexibilizam esquema ou otimizam padrões de acesso específicos.

## Práticas
- Modelagem guiada por domínio (limites claros, chaves naturais/surrogates, constraints para invariantes).
- Índices e consultas: medir seletividade, custo e efeitos de escrita.
- Transações e isolamento (ACID); escolher níveis por caso de uso.

## Distribuição
- Replicação e particionamento: trade-offs de consistência, latência e disponibilidade (ver [[Sistemas Distribuídos/Teorema CAP|Teorema CAP]]).
- Estratégias de migração/esquema: versionamento, backfills, expand/contract.

## Ligações
- [[Backend]], [[API]], [[Álgebra Relacional]], [[SQDelight]], [[Sistemas Distribuídos/Sistemas Distribuídos|Sistemas Distribuídos]].

