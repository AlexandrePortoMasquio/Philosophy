---
title: Testes Unitários
updated: 2025-09-13
---

“Testes unitários” verificam, de forma automatizada e localizada, contratos de pequenas unidades de código. Focam entradas, saídas e efeitos observáveis, isolando dependências por substituições controladas quando necessário. O objetivo é tornar regressões visíveis cedo e apoiar evolução segura do desenho.

## Exemplo
Para cálculo de tributos, casos mínimos e de borda confirmam alíquotas, isenções e arredondamentos. Dependências externas (repositórios, relógios, serviços) são substituídas por dobras com comportamento definido para que o teste observe apenas o contrato da unidade.

## Por que importa
Testes unitários reduzem custo de mudança ao detectar quebras no nível em que surgem. Ajudam a explicitar contratos, orientar refatorações e documentar decisões por exemplos executáveis.

## Cuidados e limites
Testes frágeis (acoplados a detalhes internos) geram manutenção excessiva; ausência de casos de borda cria confiança ilusória. Cobertura não substitui relevância: convém priorizar cenários críticos e invariantes do domínio.

## Relações
[[Desenvolvimento de Software]] · [[SOLID]] · [[Precisificação]] · [[Software]]
