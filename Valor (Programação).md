---
title: Valor (Software)
updated: 2025-09-16
---
Derivado de [[Software]], [[Programação]]

## Definição

(0 revisar) Em programação, valor é o conteúdo de um [[Dados (Software)|dado]], independente de sua localização ou identidade em memória. Possui semântica de igualdade por conteúdo (dois valores iguais quando todas as suas partes coincidem) e costuma ser imutável, o que o distingue de entidades referenciadas por identidade (objetos com ciclo de vida próprio). A noção ampara modelos previsíveis: o que um valor “é” não depende do lugar onde está, mas do que contém. Ver também [[Dados (Software)]].

## Funcionalidade

Valores circulam entre funções, processos e serviços por cópia ou por referências que preservam semântica por conteúdo. Imutabilidade simplifica raciocínio e concorrência, reduz efeitos colaterais e facilita [[Teste (Software)]]. Igualdade e ordenação devem ser definidas com precisão; hash estável e consistente permite uso como chave em coleções. Em fronteiras de sistema, valores são serializados segundo contratos explícitos; versionamento preserva compatibilidade e evita ambiguidade semântica. Em termos de [[Memória (Software)]], optar por valores implica avaliar custos de cópia vs compartilhamento, evitando estruturas excessivamente pesadas.

## Casos de Uso

Modelagem de domínio com “objetos de valor” (ex.: dinheiro, e‑mail, datas/intervalos) que têm identidade por conteúdo e invariantes claros; mensagens entre serviços e eventos imutáveis que sustentam reprocessamento; chaves de cache que exigem igualdade/hash corretos; modelos de UI imutáveis em arquiteturas reativas (Compose/SwiftUI) para atualizar telas por diffs de valor. Exemplo cotidiano: comparar preços ou coordenadas por conteúdo, e não por identidade de objeto, evita falsos positivos/negativos e torna o comportamento reprodutível.

