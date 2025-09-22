---
title: SOLID
updated: 2025-09-13
---
Em [[Programação]], “SOLID” é um conjunto de princípios de design que orienta coesão, separação de responsabilidades e controle de dependências. Servem como heurísticas para tornar [[Módulo (Software)|módulos]] mais previsíveis, substituíveis e verificáveis, favorecendo evolução com menor acoplamento e maior clareza de contrato.

## Princípios (síntese)
- [[Princípio de Responsabilidade Única]]: cada unidade responde por uma razão de mudança.
- [[Princípio Aberto/Fechado]]: estender sem modificar o núcleo estável do módulo.
- [[Princípio de Substituição de Liskov]]: tipos derivados preservam as promessas observáveis dos básicos.
- [[Princípio de Segregação de Interfaces]]: contratos pequenos e específicos evitam dependências desnecessárias.
- [[Princípio de Inversão de Dependência]]: dependências apontam para abstrações estáveis, não para detalhes voláteis.

## Cuidados e limites
Aplicação literal e universal degrada em formalismo estéril: princípios servem a finalidades. Responsabilidade “única” depende do recorte adotado; extensibilidade prematura pode introduzir indireções supérfluas. Convém priorizar invariantes reais do domínio, tornar contratos verificáveis e aceitar exceções quando a simplicidade ou o desempenho assim o exigirem.

## Relações
[[Desenvolvimento de Software]] · [[Precisificação]] · [[Teste Unitário]] · [[Software]]
