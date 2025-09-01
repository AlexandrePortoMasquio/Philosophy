---
title: Port (KMP)
tags: [kmp, arquitetura, ports]
created: 2025-08-31
updated: 2025-08-31
---

## Ideia
- Porta (port) é uma interface estável no [[Domain|domínio]] que descreve o que o sistema precisa (contrato), não como é feito. Permite trocar implementações sem tocar em regras de negócio ou UI.

## Tipos de portas
- Portas de entrada (driving ports): interfaces de aplicação/uso (p.ex., casos de uso) que o exterior invoca para solicitar comportamento do sistema. Expressam intenções do negócio (o “o quê”).
- Portas de saída (driven ports): interfaces que o domínio usa para depender de serviços externos (p.ex., repositórios, gateways, clock, mensageria). Permitem trocar infraestrutura sem alterar regras.

## O que NÃO é uma porta (geralmente)
- Abstrações de UI/presentation (p.ex., interfaces de ViewModel, Presenter) — são detalhes de apresentação, não fronteiras do domínio.
- Interfaces internas de infraestrutura (p.ex., DAO, client HTTP específico) que não cruzam a fronteira do domínio.
- Tipos que expõem “como” (protocolo, endpoint, SQL) em vez de “o quê” (intenção/resultado).

## Heurísticas para reconhecer uma porta
- Vive no [[Domain|domínio]] (ou camada de aplicação) e não referencia frameworks/plataformas.
- É implementada fora do domínio (na infraestrutura/apresentação).
- Descreve capacidades/intenções estáveis (contratos), não detalhes técnicos.
- Facilita testes por substituição (fakes/stubs) e evolução por troca de adapters.

## Benefícios
- Testabilidade: fakes substituem adapters reais em testes sem rede/DB.
- Portabilidade: o mesmo contrato funciona em múltiplas plataformas (útil em [[Kotlin]] Multiplatform).
- Evolução: mudanças de API/DB ficam atrás de adapters; portas preservam estabilidade de negócio e da UI.

## Diagrama (driving vs driven)
```
     (Entrada)
 UI / Controllers / Facade  ──▷  Driving Ports (Casos de Uso)
                                  │
                                  ▼
                              [[Domain]]
                                  │
                                  ▼
                            Driven Ports (Repo/Gateways/Clock)
                                     ▲
                                     │
         (Saída)               Adapters de Infra (HTTP/DB/etc.)
```
Princípio: o domínio depende apenas de portas; adapters (entrada/saída) dependem do domínio e implementam as portas.

## No desafio KMP (exemplos)
- Contratos de repositório (saída): interface de repositório que retorna `AppResult<T>` e oculta cache/rede.
- Fontes de dados (saída): interfaces de dados remoto/local como portas para infraestrutura.
- Casos de uso (entrada): interfaces que expressam intenções acionadas pela UI.
- Tipos de erro/resultado: `DomainError` e `AppResult` compõem a superfície estável para estados previsíveis na UI.

## Por quê
- Testabilidade: fakes substituem adapters reais em testes.
- Portabilidade: o mesmo contrato roda em Android/iOS (e Web) via [[Kotlin]] Multiplatform.
- Evolução: mudanças na API/DB ficam atrás de adapters; portas preservam estabilidade.

## Ligações
- [[Domain]] · [[Adapter]] · [[Facade]] · [[Ciência da Computação/Engenharia de Software/Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]]
