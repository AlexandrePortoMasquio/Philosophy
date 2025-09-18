---
title: Dados (Software)
updated: 2025-09-15
---

## Definição

Dados, em software, são representações formais que um programa manipula para produzir resultados, decidir ações e comunicar estados. Assumem tipos e estruturas que delimitam formatos, valores válidos e operações possíveis; distinguem‑se de [[Informação]] enquanto interpretação significativa em um contexto. Podem residir em [[Memória (Software)]] durante a execução ou ser preservados por [[Persistência (Software)]], conforme a finalidade.

## Funcionalidade

O tratamento de dados envolve definir modelos e contratos (tipos, esquemas), transformar representações (serialização/desserialização), validar invariantes e controlar versões ao longo do tempo. Estruturas adequadas (listas, mapas, árvores) condicionam custos de acesso e atualização; escolhas de codificação (binário ou texto) afetam compatibilidade e desempenho. Clareza de nomes, estados e erros evita ambiguidade; precisão de unidades e formatos reduz perdas e confusões em fronteiras entre sistemas.

## Casos de Uso

Modelagem de entidades de domínio (por exemplo, cliente e pedido), troca de mensagens entre serviços (JSON, Protobuf), armazenamento em bancos de dados e registro de eventos para auditoria. Exemplo cotidiano: um cadastro com campos obrigatórios e formatos definidos impede entradas inválidas e facilita integração; uma migração de esquema bem especificada permite evoluir o sistema sem interromper consumidores. Em aplicações móveis, reduzir dados carregados e padronizar formatos melhora tempo de resposta e consumo de recursos.

