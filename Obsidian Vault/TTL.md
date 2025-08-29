---
title: TTL (Time to Live)
tags: [cache, offline-first]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Tempo de vida de um item em cache. Após excedido, considera-se vencido e solicita-se refresh (manualmente ou em segundo plano).

## Uso no KMP
- Política offline-first: `TTL = 24h` para dados de catálogo. Ao abrir o app, usa cache; se houver rede, faz refresh e reconcilia (insertOrReplace).
- Invalidação adicional: mudança de versão de schema ou logout. Ajustar TTL conforme domínio.
 
## Implementação sugerida
- Persistir `updatedAt` no banco para cada item; comparar com `Clock.now()`.
- Se `now - updatedAt > TTL`, considerar expirado; agendar refresh em segundo plano e atualizar cache.
- Expor estado para UI sem bloquear: mostrar dados existentes e sinalizar refresh.

## Ligações
- [[KMP]] · [[SQLDelight]] · [[Data]]
