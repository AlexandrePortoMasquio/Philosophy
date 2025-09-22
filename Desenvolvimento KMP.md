---
title: Desenvolvimento KMP
updated: 2025-09-21
---
Derivado de [[KMP]]

## Definição

Desenvolvimento KMP é a prática de organizar e produzir software em Kotlin Multiplatform com uma base comum e alvos distintos (JVM/[[Android]], iOS/Native, [[JavaScript]]). A intenção é compartilhar lógica de domínio, dados e regras, preservando integração nativa e comportamento adequado em cada plataforma. O projeto estrutura‑se por source sets (por exemplo, `commonMain`, `androidMain`, `iosMain`) e pelo mecanismo `expect/actual` para pontos de variação inevitáveis.

Em termos práticos, camadas de domínio, parsing e regras de negócio residem no módulo comum; interfaces de usuário, permissões e integrações de sistema ficam locais a cada alvo. O desenho enfatiza fronteiras claras e contratos estáveis para evitar vazamentos de detalhes de plataforma para o núcleo compartilhado.

## Princípios

* [[SOLID]]

## Funcionalidade

A configuração declara alvos e dependências por source set e define como o código comum é emitido para cada destino (ver [[Compilação (KMP)]]). Nas bordas, adaptadores `expect/actual` encapsulam diferenças de tempo, arquivos, rede, concorrência e data/hora. A gestão de memória e coleta difere por plataforma; convém projetar dados imutáveis e minimizar transferências de objetos pesados entre camadas (ver [[Coleta de Lixo (KMP)]]).

Verificações de disponibilidade e versões da [[API de Destino]] orientam chamadas permitidas e alternativas quando necessário. Testes priorizam o módulo comum com `kotlin.test` e, por alvo, exercitam as integrações específicas; relatórios consolidados ajudam a manter regressões sob controle. Publicação e consumo de artefatos seguem formatos de cada ecossistema, mantendo contratos de tipos e nulidade.

## Casos de Uso

Aplicativos móveis que compartilham domínio, acesso a dados e validações: a mesma lógica compila para Android e iOS; a UI e as permissões permanecem locais. Benefícios incluem redução de duplicação, correções centralizadas e coerência de regras sob plataformas distintas, sem sacrificar experiência nativa.

Bibliotecas multiplataforma que expõem API comum com implementações específicas por alvo: publicação coordenada para JVM, iOS/Native e JS. Boas práticas incluem limitar acoplamento às APIs de cada plataforma, explicitar pontos de variação e medir impacto em tamanho, inicialização e consumo de recursos ao longo dos alvos suportados.

