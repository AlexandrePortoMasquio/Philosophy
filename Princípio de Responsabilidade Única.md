---
title: Princípio de Responsabilidade Única
updated: 2025-09-13
---

Cada unidade deve responder por uma razão de mudança. O recorte identifica uma responsabilidade coesa e separa preocupações distintas para reduzir acoplamento acidental. Ao fixar um propósito único, facilita substituição, verificação e evolução localizada.

## Exemplo
Em emissão de notas fiscais, validação de campos, cálculo de tributos e persistência são responsabilidades distintas. Unidades que misturam esses papéis dificultam teste e alteração de regras; a separação permite trocar o cálculo sem tocar a persistência.

## Cuidados e limites
“Única” depende do recorte: granularidade excessiva cria indireções inúteis; granularidade grossa acumula motivos variados de mudança. Convém alinhar o recorte a invariantes de domínio e fronteiras operacionais estáveis.

## Relações
[[SOLID]] · [[Desenvolvimento de Software]] · [[Precisificação]]

