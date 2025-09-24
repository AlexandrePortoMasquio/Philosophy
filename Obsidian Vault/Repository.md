---
title: Repository
tags: [arquitetura, dados]
created: 2025-09-22
updated: 2025-09-22
---
[[MVVM]], [[Clean Architecture]], [[Arquitetura KMP]]
## Definição

Repositório é a abstração que oferece ao domínio um contrato estável para ler e escrever modelos, ocultando fontes e detalhes técnicos de dados (rede, banco, cache). Trata-se de uma porta de saída: a interface vive no [[Domain|domínio]] e descreve capacidades em termos do que é necessário, enquanto sua implementação pertence à camada de dados como [[Adapter|adaptador]].

## Por que o UseCase não chama a camada de dados diretamente? Para que existe o adapter?

Porque a camada de aplicação deve depender de contratos estáveis, não de detalhes técnicos, pelo [[Princípio de Inversão de Dependência]] (DIP). O repositório funciona como porta de saída: descreve capacidades necessárias em termos do domínio e oculta protocolos, esquemas e formatos externos.

Por exemplo, um [[UseCase]] precisa de um certo dado. O repository se responsabiliza em fornecer esse dado, mas ele pode, em circunstâncias diferentes, chamar esse dado de classes diferentes do data layer. O UseCase não deve ter conhecimento de como os dados serão obtidos, mas apenas de quais dados. Por isso, ele chama o repository, e não o data layer.

O caso de uso orquestra regras e sequências; delega ao repositório a obtenção e a persistência, preservando a inversão de dependência e a testabilidade.

O adapter existe para implementar o contrato do repositório com tecnologias concretas (HTTP, banco, cache) e fazer a tradução entre modelos técnicos (DTO, linhas de banco) e tipos do domínio, além de converter exceções de infraestrutura em erros do domínio. A substituição de cliente HTTP ou de base de dados ocorre apenas no adapter, sem alterar casos de uso nem modelos centrais.

## Funcionalidade

Um repositório consolida múltiplas fontes (remota e local), aplica políticas simples de consistência (por exemplo, cache com expiração, atualização e reconciliação por chave) e mapeia estruturas técnicas para tipos do domínio, convertendo erros de infraestrutura em erros do domínio. Não define regras do negócio nem a ordem da ação; essas decisões pertencem aos casos de uso. O efeito é separar “como obter/persistir” de “o que fazer” em benefício da clareza e da testabilidade.

## Casos de Uso

Casos de uso invocam repositórios para obter ou persistir dados sem conhecer rede ou banco: “listar produtos”, “buscar detalhe”, “salvar preferência”. Em testes, fakes de repositório substituem implementações reais para cobrir fluxos de aplicação sem I/O. Em arranjos limpos, a troca de infraestrutura (cliente HTTP, base de dados) ocorre na [[Data Layer]] sem impacto no contrato consumido pelo domínio.
