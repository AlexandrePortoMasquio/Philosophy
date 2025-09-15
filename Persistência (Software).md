---
title: Persistência (Software)
updated: 2025-09-14
---

Em [[Software]], Persistência é a capacidade de registrar e conservar estados e dados de modo durável, permitindo recuperá-los após encerramentos, falhas ou migrações. O armazenamento pode ocorrer em bancos de dados, arquivos ou outros meios estáveis; o essencial é que a informação sobreviva ao processo que a produziu. Exemplo cotidiano: compromissos anotados em um caderno permanecem acessíveis no dia seguinte, independentemente de o telefone estar ligado.

## Por que importa

Sustenta continuidade de operação, recuperação de erros e rastreabilidade, além de permitir cooperação entre tempos e dispositivos distintos. Ao separar regras de negócio dos detalhes de gravação e leitura, aumenta-se a clareza, a testabilidade e a substituibilidade de tecnologias, o que reduz o custo de mudança. Esquemas explícitos e contratos estáveis evitam ambiguidades e perdas silenciosas de informação.

## Cuidados e limites

Misturar regra de negócio com detalhes de armazenamento cria acoplamento e dificulta mudanças; convém isolar o acesso a dados atrás de contratos claros, fazendo o domínio depender de abstrações. Decisões de persistência implicam compromissos entre integridade, latência e complexidade; sincronização inadequada e gravações parciais induzem inconsistências. Privacidade e segurança requerem parcimônia na coleta, criptografia adequada e controle de acesso proporcional à sensibilidade dos dados.

## Relações
[[Desenvolvimento de Software]] · [[Clean Architecture]] · [[Princípio de Responsabilidade Única]] · [[Precisificação]]

