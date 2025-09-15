---
title: Kernel (Software)
updated: 2025-09-15
---
Derivado de [[Software]]
## Definição

Kernel é o núcleo do sistema operacional responsável por mediar o uso do [[Hardware]] por processos de usuário e serviços do próprio sistema. Fornece abstrações fundamentais (processos e [[Thread (Software)]], memória, arquivos, rede, dispositivos) e aplica políticas de isolamento, segurança e compartilhamento de recursos. Em termos práticos, viabiliza que programas executem em um ambiente controlado, independente das particularidades do hardware.

## Origem

TODO

## Funcionamento

Opera em modo privilegiado do processador, respondendo a interrupções de hardware e a chamadas de sistema oriundas do espaço de usuário. Gerencia escalonamento de CPU, alocação e proteção de memória, sistemas de arquivos e drivers de dispositivo; coordena comunicação entre processos e transições de energia. Interfaces estáveis (syscalls e subsistemas) separam o núcleo das aplicações, permitindo evolução do sistema sem quebrar contratos essenciais.

## Casos de uso

Em computadores pessoais e servidores, o kernel sustenta multitarefa, rede e armazenamento persistente; em dispositivos móveis, acrescenta políticas de economia de energia, segurança reforçada e mediação de sensores; em sistemas embarcados, prioriza previsibilidade temporal e footprint reduzido. Exemplos: Linux (diversas distribuições e Android), XNU (macOS/iOS), NT (Windows) e microkernels como seL4 em aplicações críticas.
