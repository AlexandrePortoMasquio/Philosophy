---
title: Disco (Software)
updated: 2025-09-15
---

## Definição

Em software, “disco” designa o dispositivo de armazenamento persistente exposto como dispositivo de blocos pelo sistema operacional. Abrange tanto unidades magnéticas (HDD) quanto unidades de estado sólido (SSD/flash). Do ponto de vista do programa, apresenta‑se como um espaço endereçável em blocos no qual sistemas de arquivos e bancos organizam [[Dados (Software)]] de forma durável, distinto da [[Memória (Software)]], que é volátil.

## Funcionalidade

O [[Kernel (Software)]] media acesso por filas e políticas de escalonamento, mantém caches de leitura/escrita e aplica mecanismos de integridade ao persistir alterações. Padrões de acesso (sequencial ou aleatório) e características do meio (latências mecânicas em HDD, escrita por páginas/erase em SSD) influenciam fortemente o tempo de resposta. Em SSD, comandos de descarte (TRIM) ajudam a manter desempenho ao longo do uso.

## Casos de Uso

Instalação de sistemas e aplicações, bases de dados, bibliotecas de mídia e logs de auditoria. Exemplo cotidiano: importar uma grande coleção de fotos é mais rápido quando arquivos são gravados de forma contígua; atualizações frequentes de pequenos arquivos beneficiam‑se de formatos e configurações que agrupam operações. Em ambientes móveis, espaço e desgaste de flash recomendam rotacionar logs e evitar escritas supérfluas. Ver também: [[Persistência (Software)]].

