---
title: AAB (Android)
tags: [android, distribuição]
created: 2025-09-15
updated: 2025-09-15
---
[[Android]]
## Definição

AAB (Android App Bundle) é o formato de publicação preferencial para a [[Play Store]]: um pacote que descreve módulos, recursos e códigos de um [[Aplicativo (Android)]], permitindo que a loja gere [[APK (Android)]]s específicos por dispositivo. Diferentemente do APK monolítico, o AAB não é instalável diretamente; serve como insumo para geração e assinatura de APKs sob a infraestrutura de distribuição.

## Funcionalidade

O bundle organiza um [[Módulo (Software)]] base e, opcionalmente, módulos dinâmicos (entrega on‑demand). A Play Store, via Play App Signing, recebe o AAB, mantém a chave de assinatura (opcionalmente) e produz conjuntos de APKs com divisões por ABI, densidade e idioma, reduzindo tamanho de download e instalação. Ferramentas como `bundletool` permitem gerar e testar localmente conjuntos de APKs a partir do AAB para um dispositivo‑alvo específico.

## Casos de Uso

Publicação em canais internos, abertos ou por etapas (internal/alpha/beta/production) na Play Store, com entrega otimizada e suporte a recursos dinâmicos. Exemplo cotidiano: um app com módulo de realidade aumentada é entregue como feature on‑demand; usuários que não ativam o recurso não baixam seu código. Fora da Play Store, quando se exige sideload, gera‑se um APK instalável específico em vez de AAB.

