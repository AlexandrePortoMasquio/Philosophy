---
title: APK (Android)
tags: [android, empacotamento]
created: 2025-09-15
updated: 2025-09-15
---

## Definição

APK (Android Package) é a unidade de empacotamento e instalação de um [[Aplicativo Android]] no [[Android]]. Reúne manifest, recursos, bytecode [[DEX (Dalvik Executable)|DEX]] e bibliotecas nativas, e deve ser assinado por um certificado do desenvolvedor. O gerenciador de pacotes do sistema valida a assinatura e instala o app em sandbox próprio por processo/UID.

## Funcionalidade

Durante a build, o sistema empacota classes, recursos e metadados, alinha o arquivo (zipalign) e aplica o esquema de assinatura (v1/v2/v3/v4). A verificação ocorre no dispositivo antes da instalação. Em distribuição direta (fora da Play Store), o APK monolítico contém tudo o que o dispositivo precisa; quando há entrega por conjuntos (splits), múltiplos APKs específicos podem ser instalados em conjunto (base + configs) para ABI, densidade e idiomas. A execução ocorre sobre [[ART (Android Runtime)|ART]], que carrega o DEX e otimiza conforme políticas do sistema.

## Casos de Uso

Instalação local para desenvolvimento e QA, distribuição interna e lojas alternativas. Exemplo cotidiano: subir um build de teste para a equipe instalar via gerenciador de pacotes ou `adb install`, garantindo que a assinatura de debug/release corresponda à versão instalada. Para publicação na Play Store, utiliza‑se preferencialmente [[AAB (Android)]], do qual a loja deriva APKs otimizados para cada aparelho.

