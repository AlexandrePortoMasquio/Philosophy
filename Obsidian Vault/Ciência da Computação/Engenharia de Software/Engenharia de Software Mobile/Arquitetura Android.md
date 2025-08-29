---
title: Arquitetura Android
tags: [mobile, android, arquitetura]
created: 2025-08-28
updated: 2025-08-28
---

## Mapa Rápido
- Acima: [[../Arquitetura de Software|Arquitetura de Software]] · [[../../Sistemas Operacionais/Sistemas Operacionais|Sistemas Operacionais]] · [[Arquitetura MVVM]]
- Lado: [[Android]] · [[iOS]] · [[Multiplataforma]] · [[KMP]]

## Ideia
- Estruturar apps Android em camadas com fluxos previsíveis e limites claros: UI (Compose), Apresentação (MVVM/UDF), Domínio (casos de uso), Dados (repositórios, fontes locais/remotas).
- Otimizar trade-offs entre manutenibilidade, testabilidade e desempenho sob restrições móveis (bateria, latência de rede, memória).

## Camadas e Fluxo de Dados
- UI: Compose + State hoisting; evita lógica de negócio na UI.
- Apresentação: ViewModel com coroutines/Flow; UDF (ações → estado) reduz efeitos colaterais.
- Domínio: casos de uso orquestram políticas de negócio.
- Dados: Repositórios consolidam fontes (Room/SQLDelight, Network com Ktor/Retrofit); caches e políticas offline‑first.

## Decisões Centrais
- Estado: imutabilidade local, fontes únicas de verdade; [[Injeção de Dependência]], ciclo de vida.
- Concorrência: coroutines (Dispatchers), cancelamento estruturado, backpressure com Flow.
- DI: Koin (somente na apresentação); limites modulares (feature modules).
- Navegação: Navigation Compose, rotas estáveis, deep links.
- Observabilidade: logs, métricas, tracing, ANR/Crash.

## Testes
- Unidade (domínio), instrumentados (DAO, navegação), UI (Compose Testing), contratos de API.

## Ligações
- [[../Arquitetura de Software|Arquitetura de Software]] · [[Android]] · [[Multiplataforma]] · [[KMP]] · [[Engenharia de Software/Processos|Processos]] · [[Engenharia de Software/Testes|Testes]] · [[Engenharia de Software/Desempenho|Desempenho]]

## Application vs Composable Root (Android)
- Application (ex.: `MyAppApplication`): inicializa DI (Koin), logs, configs globais e providers (SqlDriver). Padrão profissional.
- Composable raiz (ex.: `RootApp`): tema, navegação, estado de UI. Chamado pela `MainActivity` via `setContent { ... }`.
- Nomenclatura: evite nomes genéricos (`App.kt`). Prefira `MyAppApplication.kt` e `RootApp.kt`.

