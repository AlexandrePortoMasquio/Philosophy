---
title: Cliente
updated: 2025-09-13
---
Relacionado a: [[Software]], [[Programação]] 

## Definição

Em [[Programação]], componente que consome um contrato de software. Não se confunde com “[[Usuário]]”, que ocupa o papel de operação e acesso a funcionalidades.

## Relações

Interage com contratos expostos por interfaces e serviços (ver [[Contrato (Software)]]); consome APIs e repositórios por meio de adaptadores e protocolos; é invocado por camadas de apresentação/controladores que delegam trabalho à lógica consumida. Em resumo, relaciona‑se “para baixo” com provedores (serviços, módulos) e “para cima” com chamadores (UI, controladores), mantendo acoplamento ao contrato e não à implementação.

## Exemplo

Em um projeto KMP, “cliente” nomeia o componente que consome um contrato de software. Exemplo: no `commonMain`, declara‑se `AuthService`; sua implementação usa um `HttpClient` para chamar `/login` e `/me`, sendo cliente da API remota. Nas plataformas, `androidMain` e `iosMain` invocam `AuthService` a partir da UI e, assim, são clientes da interface interna. Em todos os casos, “cliente” designa o código que consome uma API (remota ou local), não uma entidade externa.
