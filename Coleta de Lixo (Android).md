---
title: Coleta de Lixo (Android)
updated: 2025-09-16
---
Derivado de [[Coleta de Lixo (Software)]]

## Definição

No [[Android]], a coleta de lixo (GC) é parte do runtime [[ART (Android Runtime)|ART]] responsável por recuperar memória ocupada por objetos inacessíveis no heap do processo, mantendo aplicações sob limites de uso e preservando estabilidade. O objetivo é equilibrar segurança e fluidez de interface, reduzindo vazamentos e pausas perceptíveis em cenários interativos.

## Funcionalidade

O ART utiliza estratégias geracionais e concorrentes: coleções jovens frequentes e curtas, coleções completas ocasionais, compactação seletiva e barreiras para manter coerência com threads de aplicação. Políticas ajustam gatilhos conforme pressão de heap e classe de memória do app; o sistema emite sinais de economia de memória (trim) para que aplicações reduzam caches. Pausas de GC que coincidam com renderização podem causar jank; medições com [[Perfetto]] ajudam a correlacionar alocações, pausas e frames perdidos.

Boas práticas incluem limitar alocações no caminho quente (rolagem/listas), reutilizar buffers e bitmaps, preferir estruturas adequadas ao padrão de acesso e liberar referências a objetos grandes quando não forem mais necessários. Em camadas multiplataforma, evitar cópias redundantes ao cruzar fronteiras. Ver também: [[Coleta de Lixo (KMP)]].

## Casos de Uso

Apps com listas e feeds extensos, processamento de imagens e networking intensivo: reduzir picos de alocação e dimensionar caches evita pausas visíveis. Exemplo cotidiano: a abertura de uma tela engasga devido a parsing pesado e alocações na thread principal; o traço revela pausas do GC durante a composição de UI — a correção desloca trabalho para threads de fundo e suaviza o perfil de alocação.

