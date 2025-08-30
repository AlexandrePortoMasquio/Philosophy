---
title: Padrões de Projeto (foco KMP)
tags: [arquitetura, padrões, kmp]
created: 2025-08-29
updated: 2025-08-29
---

## Padrões úteis no KMP
- Repository: abstrai fontes de dados; contrato no domínio; implementação em data.
- Use Case: orquestra regra de negócio; expõe `AppResult`/`UiState`.
- Mapper: converte DTO/DbRow → Domain; funções puras testáveis.
- Adapter: integra APIs externas (Ktor/DB) ao contrato interno.
- Strategy: políticas de retry/backoff/TTL pluggáveis.
- Decorator: logging/metrics em volta de repositórios/use cases.

## Diretrizes
- Aplicar SRP/ISP/DIP na definição de contratos; evitar interfaces “gordas”.
- Preferir imutabilidade e resultados tipados (sealed) para estados/erros.
- Evitar vazar tipos de plataforma no shared.

## Ligações
- [[Princípios SOLID]] · [[KMP]] · [[../../Data Layer]]
