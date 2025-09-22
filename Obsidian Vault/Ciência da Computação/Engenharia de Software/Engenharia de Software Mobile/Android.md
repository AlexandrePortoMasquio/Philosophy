---
title: Android
tags: [android]
created: 2025-08-29
updated: 2025-09-15
---
## Definição

Android é uma [[Plataforma (Programação)]] [[Desenvolvimento Mobile|móvel]] baseada em [[Linux]] que fornece um sistema operacional, um conjunto de APIs e um ambiente de execução para aplicações. Oferece modelo de permissões, distribuição por lojas e suporte a múltiplos fabricantes e formatos de dispositivo. O objetivo é permitir aplicações com integração a recursos do aparelho sob diretrizes comuns de segurança e experiência.

## Base do Sistema em Linux

O Android assenta-se sobre o [[Kernel (Software)]] [[Linux]], acrescido de mecanismos e políticas específicos: Binder para IPC, gerência de processos com cgroups e prioridades, controle de energia (wakelocks) e segurança reforçada com SELinux em modo enforcing. Na camada de usuários, a libc Bionic, o conjunto de serviços do framework (System Server) e as interfaces HAL (AIDL/HIDL) mediam acesso a hardware e organizam permissões, isolando cada aplicação em processo e UID próprios. Essa base fornece isolamento, desempenho e portabilidade entre fabricantes, mantendo um núcleo comum de execução.

## Funcionamento

Aplicações são empacotadas em [[APK (Android)]]/[[AAB (Android)]], assinadas e instaladas pelo gerenciador do sistema. Cada app executa em processo próprio com sandbox, interage por intents e serviços, e observa eventos de ciclo de vida (criação, pausa, retomada, destruição). Recursos como armazenamento, rede, sensores e câmera são acessados por APIs com controle de permissões; tarefas em segundo plano seguem políticas de economia de energia e limites de execução.

## Casos de uso

Comunicação, navegação, captura e edição de mídia, serviços financeiros, saúde, educação, entretenimento e soluções corporativas com integrações específicas de hardware. Em contextos dedicados, Android equipa terminais de pagamento, coletores, quiosques e dispositivos embarcados gerenciados por políticas de empresa.

## DEX/ART

[[DEX (Dalvik Executable)]] é o formato de bytecode utilizado por aplicações Android; reúne classes e métodos em arquivos como `classes.dex` dentro do pacote do app. [[ART (Android Runtime)]] é o ambiente de execução responsável por carregar e executar esse bytecode, combinando interpretação, compilação just‑in‑time e ahead‑of‑time conforme políticas do sistema. Esse arranjo viabiliza portabilidade entre arquiteturas e otimizações no dispositivo, reduzindo tempo de arranque e melhorando desempenho ao longo do uso.
## Ver também
- [[Arquitetura Android]]
- [[KMP]] · [[Arquitetura KMP]]
- [[Perfetto]]

## TODOs
- Definir `MyAppApplication` e `RootApp` como nomes finais.
- Criar guideline de navegação e estados de tela.
- Checklist de acessibilidade (tamanhos de fonte, contraste, talkback).
