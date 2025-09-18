---
title: Desenvolvimento Mobile
updated: 2025-09-15
---

## Definição

O desenvolvimento mobile é a concepção, implementação e manutenção de [[Aplicação (Software)|aplicações]] destinadas a [[Dispositivo Móvel|dispositivos móveis]], coordenando interface, acesso a recursos do aparelho ([[Sensores (Mobile)]], câmera, [[Armazenamento (Mobile)]] e [[Rede (Mobile)]]) e [[Ciclo de Vida (Software)]] específico de [[Plataformas (Mobile)]]. O objetivo é oferecer capacidades úteis sob restrições de tela, energia, conectividade e segurança, com comportamento consistente diante de interrupções e variações de contexto.

## Tipos

Há abordagens nativas (Android com Kotlin/Java; iOS com Swift/Objective‑C), multiplataforma compilada para binários nativos ([[KMP|Kotlin Multiplatform]], [[Flutter]] em modo [[AOT]]), camadas híbridas que utilizam componentes web dentro de contêineres nativos (Cordova, Capacitor) e aplicações web progressivas (PWA) servidas pelo navegador. A escolha combina requisitos de acesso a APIs do sistema, desempenho, experiência de interface e custo de manutenção entre plataformas.

## Diferenças e peculiaridades

Soluções nativas oferecem acesso imediato às APIs da plataforma, integração fina com o ciclo de vida e máxima fidelidade de interface, ao custo de manter bases separadas. Multiplataforma como [[KMP]] preserva o domínio compartilhado e permite implementações específicas nas bordas (UI, dispositivos), reduzindo duplicação sem impor um único toolkit de interface. Flutter unifica UI com renderização própria e alto grau de consistência visual, mas demanda adaptação para padrões nativos e peso de runtime. Híbridos e PWAs aceleram entregas e reuso web, porém dependem do navegador e podem limitar acesso a recursos ou responsividade sob carga; são adequados quando requisitos de hardware e integração profunda são modestos.
