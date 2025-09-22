---
title: API de Destino
updated: 2025-09-21
---

[[KMP]] [[Android]] [[Compilação (KMP)]] [[Código de Alvo]]

## Definição

API de destino é o conjunto de interfaces, tipos e serviços oferecidos pela plataforma alvo (sistema operacional, runtime ou framework) com as quais um programa deve ser compatível em compilação e execução. Delimita símbolos disponíveis, contratos de tipos, modelos de erro e restrições de uso; quando versionada, inclui o nível/versão de API que condiciona o acesso a recursos. Funciona como fronteira entre o código próprio e o ambiente, orientando dependências e compatibilidade.

Exemplos: no Android, o nível de API define a disponibilidade de classes e métodos; em iOS, anotações de disponibilidade regulam chamadas a frameworks; em JavaScript, o alvo (navegador/engine) determina o conjunto de APIs web ou Node acessíveis.

## Funcionalidade

A seleção da API de destino no toolchain filtra chamadas permitidas, aplica verificações de disponibilidade e escolhe bibliotecas de ligação e metadados apropriados. No Android, configurar o nível mínimo/compilado governa warnings/erros e pode exigir alternativas (backs compatíveis) para recursos novos; em iOS, checagens de disponibilidade evitam chamadas indevidas; em JavaScript, o alvo define transpilações e polyfills necessários.

Em contextos multiplataforma, o mecanismo `expect/actual` direciona invocações para APIs de cada alvo, enquanto camadas de interop estabilizam diferenças de assinaturas, nulidade e threading. O código de alvo resultante preserva a semântica comum e adapta forma e convenções às exigências de cada ambiente.

## Casos de Uso

Definir um nível mínimo de API que maximize cobertura de dispositivos sem bloquear funcionalidades essenciais, complementando com alternativas quando preciso. Encapsular chamadas a APIs específicas atrás de interfaces próprias para isolar mudanças de versão e facilitar testes. Em bibliotecas multiplataforma, manter uma camada fina de interop e documentar claramente requisitos de API do consumidor.

Em otimização e auditoria, inspecionar chamadas à API de destino e o código de alvo gerado ajuda a identificar riscos (métodos obsoletos, permissões, limitações de plataforma) e a ajustar decisões de compatibilidade, tamanho e desempenho.

