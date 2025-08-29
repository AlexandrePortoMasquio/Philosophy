---
title: Logging
tags: [observabilidade]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Registro estruturado de eventos do app (info/erro/debug) para diagnóstico e auditoria.

## Por que usar no KMP
- Observabilidade mínima no Shared sem acoplar a plataformas; facilita troubleshooting de rede/cache/use cases.
- Com [[Napier]], um único logger direciona para Logcat (Android) e NSLog (iOS).

## No Desafio Técnico KMP
- Ajudar a evidenciar decisões e comportamentos (erros de rede, políticas de cache) sem bibliotecas pesadas.
