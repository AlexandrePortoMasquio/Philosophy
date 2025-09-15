---
title: Princípio de Responsabilidade Única
updated: 2025-09-13
---

## Cada unidade deve responder por uma razão de mudança.

Significa que cada unidade de software — [[Módulo (Software)]], classe ou função — existe para um propósito identificável, e qualquer alteração nessa unidade deve decorrer de um único motivo coerente. Quando a mesma unidade precisa mudar por razões distintas (por exemplo, regras de negócio e detalhes de apresentação), ocorre acúmulo de responsabilidades e aumento de fragilidade: modificar uma dimensão pode afetar indevidamente a outra. Exemplo cotidiano: numa biblioteca, o catálogo registra obras e a portaria controla acesso; alterar o horário de abertura não deve exigir reescrever a catalogação.

## O recorte identifica uma responsabilidade coesa e separa preocupações distintas para reduzir acoplamento acidental.

O recorte define a fronteira semântica da unidade: decisões que variam juntas permanecem reunidas; preocupações distintas (regra de negócio, persistência, apresentação) são mantidas separadas. Essa distinção evita dependências involuntárias, reduz propagação de mudanças e torna explícito o propósito de cada parte. Exemplo cotidiano: calcular o valor do frete pertence ao domínio; armazenar o resultado pertence à persistência.

Exemplo no KMP: TODO

Ao fixar um propósito único, facilita substituição, verificação e evolução localizada.

## Aplicações em KMP
* Ver [[Arquitetura KMP]]
- Domínio no `commonMain`: regras estáveis e puras, sem dependências de plataforma.
- Interfaces no domínio para serviços voláteis (tempo, rede, armazenamento) com implementações em `androidMain` e `iosMain`.
- Dados como responsabilidade separada: mapeamento e persistência sem lógica de negócio.
- Serialização e cliente de rede isolados; troca de implementação não afeta o domínio.
- Apresentação por plataforma consome casos de uso; evitar regras de negócio na UI.
- Testes em `commonTest` validam o domínio; dublês específicos por plataforma quando necessário.


## Cuidados e limites
“Única” depende do recorte: granularidade excessiva cria indireções inúteis; granularidade grossa acumula motivos variados de mudança. Convém alinhar o recorte a invariantes de domínio e fronteiras operacionais estáveis.

## Relações
[[SOLID]] · [[Desenvolvimento de Software]] · [[Precisificação]]
