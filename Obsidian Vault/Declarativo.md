---
title: Programação Declarativa
tags: [conceitos, programação, declarativo, kmp]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Estilo em que descrevemos o resultado desejado (o “o quê”) e não o passo a passo imperativo (o “como”). O runtime/mecanismo subjacente se encarrega de aplicar as mudanças necessárias.
- Exemplos: SQL (o que selecionar), CSS (como deve aparecer), SwiftUI/Compose (árvore de UI a partir de estado).

## Benefícios
- Menos estado mutável explícito e menor acoplamento a ordem de execução.
- Maior previsibilidade e testabilidade: funções puras sobre dados → saídas estáveis.
- Composição natural: pequenas expressões e descrições que se combinam.

## Por que usar no [[KMP]]
- Interop com UIs declarativas: [[SwiftUI]] (iOS) e Compose (Android) consomem estados imutáveis e intents, casando com `Flow/StateFlow` do shared.
- Redução de divergência entre plataformas: a mesma lógica reativa/declaração de estados no shared alimenta camadas declarativas de UI distintas.
- Testabilidade: casos de uso retornam modelos/estados; snapshots e asserts independem da plataforma.

## Padrão de Uso
- Domain/Data no shared: funções puras o máximo possível; efeitos (rede/IO) isolados.
- Expor `StateFlow<UiState>` ou resultados selados (`sealed class`) no shared.
- Na borda, mapear estado → árvore de UI declarativa (Compose/SwiftUI).

## Quando evitar
- Algoritmos de baixo nível e loops críticos onde o controle fino da ordem e mutabilidade traz ganhos claros de desempenho/clareza.

## Relações
- [[Reatividade]] · [[KMP]] · [[SwiftUI]]
