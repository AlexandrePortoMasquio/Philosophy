---
title: Use Case (Aplicação)
tags: [aplicação, ports, kmp]
created: 2025-08-31
updated: 2025-08-31
---
## Definição

UseCase é um serviço de [[Aplicação (Programação)]] que realiza uma intenção do sistema de forma atômica e verificável. Define o encadeamento da ação (pré‑condições, ordem e combinações), orquestra portas de saída (repositórios, gateways, relógio, geradores) e devolve um resultado, sem conhecer detalhes de interface, banco de dados ou rede.

Opera sem estado e com fronteira clara: recebe dados por valor, invoca portas, trata erros e retorna um tipo de resultado do domínio (sucesso/falha). Exemplo simples: “efetuar login” valida credenciais, consulta o usuário, aplica política de bloqueio e produz um estado de sessão — sem interagir diretamente com widgets ou armazenamentos concretos.

## Responsabilidades

- Definir uma funcionalidade única da aplicação, e suas pré‑condições (parâmetros válidos e contexto autorizado).
- Validar entradas e autorizações; recusar pedidos incoerentes antes de acionar dependências.
- Orquestrar portas de saída (repositórios, relógio, geradores, notificadores) na ordem correta, respeitando limites transacionais.
- Impor invariantes do negócio; decidir quando confirmar ou abortar a operação.
- Tratar falhas e mapeá‑las para um resultado estável do domínio, distinguindo causas recuperáveis e definitivas.
- Garantir idempotência quando aplicável, evitando efeitos colaterais duplicados.
- Não conhecer UI nem infraestrutura; expor apenas tipos do domínio e um contrato de resultado.
- Não manter estado interno nem política de threads; o chamador define o contexto de execução.

## Por que o UseCase não mantém estado? Como isso se alinha ao SOLID?

Não mantém estado para preservar previsibilidade, reentrância e simplicidade. Cada invocação recebe dados por valor, aciona portas e devolve um resultado; manter variáveis internas ligaria o caso de uso ao ciclo de vida do processo e à concorrência, introduzindo dependências implícitas, condições de corrida e dificuldade de teste.

O arranjo está alinhado ao SOLID: SRP, porque orquestra uma única intenção sem acumular responsabilidades de memória ou sessão; DIP, porque depende de portas (abstrações) e não de implementações concretas; OCP, porque novos fluxos surgem como novos casos de uso, sem alterar os existentes. Estado durável ou transacional pertence às portas (repositórios, unidade de trabalho), não ao caso de uso.

## Por que o ViewModel precisa do UseCase, e não acessa o Repository diretamente?

O ViewModel não acessa diretamente repositórios porque isso mistura apresentação com orquestração de regras. O [[Repository]] fornece dados e políticas de acesso; o caso de uso valida entradas, combina múltiplas fontes, impõe invariantes e define o resultado como contrato da aplicação. Colocar essa lógica na ViewModel duplica fluxos entre telas, aumenta acoplamento a detalhes de dados (DTOs, paginação, cache) e enfraquece a inversão de dependência.

O que significa "validar entradas" e "impor invariantes", e por que apenas o UseCase faz isso: Validar entradas é verificar as pré‑condições do contrato do caso de uso: presença e formato dos dados, coerência semântica (p.ex., intervalos, estados permitidos) e autorizações pertinentes ao contexto. Impor invariantes é garantir que estados proibidos não sejam produzidos — por exemplo, não criar pedido sem itens, não efetivar operação fora de janela temporal definida, não exceder limites quantitativos do negócio — independentemente da origem dos dados.

Essas garantias pertencem ao caso de uso porque expressam a política da aplicação e a ordem da ação. Repositórios apenas obtêm e persistem dados segundo contratos técnicos; o ViewModel lida com ciclo de vida e apresentação.

Centralizar as regras na aplicação evita duplicação entre telas porque todas consomem o mesmo contrato e trilha de validação; a mudança de política ocorre uma única vez. Impede violações quando múltiplas fontes são combinadas: por exemplo, preço vindo do cache e estoque vindo da rede só permitem “finalizar compra” se ambos forem validados sob as mesmas restrições do caso de uso; sem essa orquestração, telas distintas tenderiam a adotar critérios divergentes. Também facilita testes: testes de unidade do caso de uso, com fakes das portas, verificam pré‑condições, invariantes e ordem das chamadas; a UI é exercitada apenas quanto à tradução de resultados em estado de tela.

Com o caso de uso como fronteira, a interface consome um único contrato estável e testável. Alterações na camada de dados (cliente HTTP, fonte local, política de retry) não vazam para a UI; testes de domínio cobrem a orquestração, e testes de ViewModel verificam apenas a transformação de resultados em estado de tela. O efeito é menor superfície de erro, reutilização entre telas e evolução independente das camadas.

## Em MVVM e Clean Architecture, em qual camada está o UseCase?

Na [[Clean Architecture]], o UseCase situa‑se na camada de [[Aplicação (Clean Architecture)|Aplicação]]: define e executa a orquestração entre entidades do domínio e portas de saída. Não pertence à interface de usuário nem à infraestrutura.

Em MVVM, a [[ViewModel]] invoca o UseCase e publica o resultado como estado de tela; repositórios e gateways (infraestrutura) implementam as portas consumidas. Em arranjos KMP, o contrato do UseCase pode residir no [[Domain|domínio]] para favorecer inversão de dependência, enquanto a implementação realiza a orquestração na camada de Aplicação.

## Ideia
- Caso de uso é um serviço de aplicação que expõe uma intenção do sistema (o “o quê”), orquestrando portas de saída (repositórios/gateways) sem conhecer UI ou infraestrutura.
- Em KMP, define‑se como interface no [[Domain|domínio]] (driving port); a implementação depende apenas de [[Port|portas]] e tipos puros (p.ex., `AppResult`).

## Diretrizes
- Foco: uma intenção clara (p.ex., “obter lista”, “buscar detalhe”).
- Sem estado interno e sem thread policy (o chamador decide contexto/dispatcher).
- Sem dependência de UI/frameworks; entrada/saída por valores.
- Sem acoplamento entre casos de uso: não chamar outro use case diretamente.

## Evitando recursividade/composição cíclica
- DI acíclica: cada caso de uso recebe apenas portas de saída (repositório, clock, etc.); não recebe outros casos de uso como dependência.
- Composição no nível superior: [[ViewModel]]/[[Facade]] agregam chamadas a múltiplos casos de uso, preservando a independência entre eles.
- Orquestradores dedicados (quando necessário): criar um “application service/coordinator” específico que coordene múltiplas operações, ainda dependendo só de portas — nunca de use cases entre si.
- Regras de módulo: o [[Domain]] não exporta fábricas que conectem um caso de uso a outro; [[Adapter]]/DI só ligam use cases → portas.
- Testes: testes de use case usam fakes de portas; inexistência de mocks de outros use cases detecta acoplamento indevido.

## Assinatura típica (Kotlin)
- Função única `invoke(params): AppResult<Out>` (ou `suspend`), com tipos de entrada/saída no domínio.

## Ligações
- [[Domain]] · [[Port]] · [[Adapter]] · [[Facade]] · [[ViewModel]] · [[Ciência da Computação/Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]]
