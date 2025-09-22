---
title: Compilação (KMP)
updated: 2025-09-21
---
Derivado de [[KMP]], [[Compilação (Programação)]]

## Definição

Em Kotlin Multiplatform, compilação é o processo que transforma [[Código de Alvo|código comum e específico de alvo]] em artefatos executáveis para plataformas distintas (JVM/[[Android]], iOS/Native, [[JavaScript]]). O projeto organiza‑se em source sets (por exemplo, `commonMain`, `androidMain`, `iosMain`) e usa o mecanismo `expect/actual` para conciliar APIs próprias de cada plataforma com a base compartilhada. O objetivo é obter um único corpo de lógica a ser emitido para múltiplos destinos, respeitando restrições e formatos de cada ambiente.

Os resultados típicos incluem: bytecode JVM (convertido a DEX no Android), binários nativos via LLVM para iOS (framework estático/dinâmico) e módulos JavaScript. A estrutura preserva interoperabilidade com ecossistemas locais (Java/ART no Android; Objective‑C/Swift no iOS; módulos JS no navegador ou Node), mantendo contratos claros nas fronteiras.

## Funcionalidade

A seleção de alvos determina back‑ends: no destino JVM/Android, o compilador emite classes e metadados Kotlin/Java, depois convertidos pelo toolchain da plataforma; no destino Native, o código é baixado para LLVM com ligações a bibliotecas do sistema e interop de C/Objective‑C (ex.: geração de cabeçalhos para consumo em Swift); no destino JS, a representação intermediária gera código JavaScript moderno. A resolução de source sets garante que o que for comum seja reutilizado e que diferenças locais apareçam apenas onde necessário.

O processo admite incrementalidade, checagens de tipos e nulidade consistentes entre alvos e integração com ferramentas de construção (por exemplo, Gradle). Artefatos publicados podem ser consumidos por aplicativos Android (AAR/JAR), por apps iOS (frameworks) e por aplicações web (pacotes JS), com versionamento e assinaturas conforme cada repositório.

## Casos de Uso

Aplicativos que compartilham domínio, rede e parsing: a lógica comum compila para AAR no Android e para um framework no iOS, enquanto camadas de UI e integração ficam locais. Padrões de I/O, datas e concorrência usam `expect/actual` para encapsular diferenças, evitando condicionais espalhadas.

Bibliotecas multiplataforma publicam um único módulo com variantes para JVM, JS e Native. Equipes reduzem custo de manutenção ao corrigir erros uma vez no código comum, mantendo desempenho e integração nativa em cada plataforma.

