---
title: Contrato (Software)
updated: 2025-09-15
---

## Definição

Contrato, em software, é a especificação estável do que um componente oferece e exige: operações disponíveis, formatos de dados, pré‑condições e pós‑condições, erros e invariantes. Serve como fronteira compreensível entre partes do sistema, permitindo substituição e evolução independente sem quebrar consumidores. Pode ser expresso por interfaces e tipos, documentação de API e testes de contrato que verificam o comportamento prometido.

## Funcionalidade

Ao separar o “o que” do “como”, o contrato reduz acoplamento e orienta desenho modular. Em arquiteturas como [[Clean Architecture]], o domínio define contratos que as bordas implementam; pelo [[Princípio de Inversão de Dependência]], políticas de negócio não dependem de detalhes. A precisão de nomes, estados e erros evita ambiguidade; versionamento explícito e compatibilidade retroativa preservam integridade quando o contrato evolui. [[Precisificação]] auxilia a tornar requisitos testáveis.

## Casos de Uso

Interfaces entre camadas (domínio↔dados), serviços em rede (REST/gRPC), plug‑ins e bibliotecas públicas. Exemplo cotidiano: um serviço de pagamento aceita pedidos com campos definidos e responde com estados claros; mudanças internas de banco ou linguagem não afetam clientes desde que o contrato se mantenha. Em KMP, contratos no código comum permitem que Android e iOS consumam a mesma API, com implementações específicas nas bordas.

