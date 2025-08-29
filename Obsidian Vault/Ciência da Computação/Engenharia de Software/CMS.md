---
title: CMS (Content Management System)
tags: [engenharia de software, cms, conteúdo]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Sistema para criar, versionar e publicar conteúdo (textos, mídia, páginas) com fluxos editoriais (perfis, revisão, aprovação) e entrega por templates ou [[API]]s.

## Tipos
- Tradicional (acoplado): edição e entrega no mesmo sistema (WordPress, Drupal clássico). Simples, porém menos flexível para múltiplos canais.
- Headless: o CMS expõe conteúdo via [[API]] (REST/[[GraphQL]]) e clientes (web/app) renderizam. Acopla menos, facilita omnichannel.
- Jamstack/estático: gera arquivos estáticos a partir de conteúdo + build; baixo custo e alta performance com limites dinâmicos.

## Quando usar
- Portais, blogs, e-commerce com catálogo editorial, landing pages frequentes, experiências omnichannel.
- Evita reinventar admin/workflows; delega a taxonomias, permissões e publicação.

## Ligações
- [[Backend]] (integrações e webhooks), [[API]] (headless), [[Banco de Dados]] (modelo de conteúdo), [[Governança]] (perfis e auditoria).

## Notas
- Modelagem de conteúdo clara (tipos, campos, taxonomias) antecipa internacionalização, SEO e reuso.

