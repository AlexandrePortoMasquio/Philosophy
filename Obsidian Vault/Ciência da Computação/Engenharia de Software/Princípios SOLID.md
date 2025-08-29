---
title: Princípios SOLID
tags: [engenharia de software, arquitetura, princípios]
created: 2025-08-28
updated: 2025-08-28
---

## Ideia
- Conjunto de princípios que aumentam coesão, reduzem acoplamento e tornam mudanças mais baratas. Não é dogma: são heurísticas guiadas por contexto, custo de mudança e feedback.

## Princípios (por extenso)
- SRP — Princípio da Responsabilidade Única (Single Responsibility Principle):
  - Uma unidade (módulo/classe) deve ter um único motivo para mudar. Promove coesão e clareza de limites.
  - Indicadores: nomes claros; dependências mínimas; testes focados.
- OCP — Princípio do Aberto/Fechado (Open-Closed Principle):
  - Entidades devem estar abertas à extensão e fechadas à modificação. Evolução por composição/polimorfismo, evitando editar código estável.
  - Indicadores: APIs estáveis; `sealed` para variantes; pontos de extensão definidos.
- LSP — Princípio da Substituição de Liskov (Liskov Substitution Principle):
  - Subtipos devem preservar contratos do tipo base; trocar implementação não muda propriedades observáveis.
  - Indicadores: testes de substituição; contratos explícitos (pré/pós‑condições, invariantes).
- ISP — Princípio da Segregação de Interfaces (Interface Segregation Principle):
  - Prefira várias interfaces específicas ao cliente a uma interface “gorda” e genérica. Consumidores dependem só do que usam.
  - Indicadores: interfaces pequenas e focadas; menos métodos “não usados”.
- DIP — Princípio da Inversão de Dependência (Dependency Inversion Principle):
  - Dependências apontam para abstrações (interfaces), não para concretos; detalhes dependem de políticas.
  - Indicadores: bordas fazem a ligação (injeção/composição); núcleo depende de portas/contratos.

## Sinais de Alerta (quando aplicar)
- Baixa coesão (classes fazem “de tudo”); alto acoplamento (muitas dependências cruzadas).
- Testes frágeis (mudanças triviais quebram muitos testes) e efeitos colaterais difusos.
- Dificuldade para introduzir uma nova variante sem tocar em múltiplos módulos.

## Anti‑padrões comuns (e correções)
- “God Object/Manager”: quebre por SRP; extraia serviços e mapeadores.
- Interface gigante de repositório: aplique ISP; separe leitura/escrita e por caso de uso.
- Switch por tipo espalhado: aplique OCP/LSP com `sealed class` + handlers registrados.
- Núcleo dependendo de SDKs: aplique DIP; crie portas no domínio e adapte nas bordas.

## Exemplos (KMP/Android)
- SRP: `UseCase` (orquestra regra) separado de `Repository` (acesso a dados) e `Mapper` (tradução de modelos).
- OCP: resultado como `sealed class Result { Success|Empty|NetworkError|Timeout }` e novas variantes com novos handlers.
- LSP: `CatalogRepositoryFake` substitui `CatalogRepository` real em testes sem mexer em consumidores.
- ISP: `ReadOnlyCatalogRepository` para telas de consulta; comandos separados das queries.
- DIP: `expect interface Clock` no shared; `actual` por plataforma injetado nas bordas.

## Enforcement (como garantir)
- Limites de módulo/pacote; visibilidades restritas; regras de dependência no Gradle.
- Testes de substituição (LSP), contratos de API, análise estática e lints.

## Ligações
- [[Arquitetura de Software]] · [[Engenharia de Software Mobile/Arquitetura KMP|Arquitetura KMP]] · [[Engenharia de Software Mobile/Arquitetura Android|Arquitetura Android]] · [[Padrões de Projeto]] · [[Engenharia de Software/Testes|Testes]]
