---
title: Codegen (Geração de Código)
tags: [build, engenharia]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Ferramentas que geram código a partir de anotações/arquivos de definição (ex.: Dagger/Hilt, Room, Protobuf, SQLDelight).

## Por que evitar em excesso
- Aumenta tempo de build e acoplamento a toolchains específicos.
- Em KMP, muitas ferramentas são plataforma‑específicas e não rodam no Shared.

## No projeto
- Preferimos Koin (sem codegen) para DI no Shared e Android.
- Usamos SQLDelight (codegen) porque fornece schema comum e APIs tipadas multiplataforma — custo/benefício favorável.
