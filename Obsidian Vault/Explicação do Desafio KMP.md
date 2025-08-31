---
title: Explicação do Desafio KMP
tags: [kmp, entrevista, arquitetura]
created: 2025-08-31
updated: 2025-08-31
---

## Objetivo
- Preparar a defesa técnica do desafio (lista/detalhe de lojas de saquê) implementado em [[Kotlin|Kotlin]] Multiplatform, cobrindo arquitetura, decisões, trade‑offs e como rodar/validar.
- Requisitos: ver [[Desafio Técnico KMP - Requisitos]].

## Arquitetura (visão geral)
- Estilo Ports/Adapters (DIP): contratos no domínio; implementações em data/feature. Facilita testes e troca de fontes de dados.
- Camadas (shared):
  - Domínio: entidades (CatalogItem), `AppResult`/`DomainError` (estado/erros tipados), repositório (contrato) e casos de uso.
  - Data: `RemoteDataSource` (Ktor) + `LocalDataSource` (SQLDelight); `CatalogRepositoryImpl` (offline‑first) com mapeadores.
  - DI simples (fábricas) expõe construção de `HttpClient`, DB e repositório. Sem framework (menor atrito e builds mais rápidos).
- UI/Plataformas:
  - Android: Compose (MVVM), usa o repositório do shared; carrega imagens com Kamel.
  - iOS: SwiftUI (MVVM), consome um Facade KMP (bridge amigável a Swift) que encapsula corrotinas/Flow.

## Decisões e por quê
- [[Ktor]] + kotlinx.serialization: leve, multiplataforma e sem reflexão; encaixa bem no shared.
- [[SQLDelight]]: esquema único e consultas tipadas; ótimo para offline‑first em Android/iOS.
- Resultado/Erro tipados: `AppResult/DomainError` evitam exceções cruzando camadas/interop, padronizando Loading/Empty/Error/Content.
- DI por fábricas: simplicidade > framework (tempo do desafio) e mantém isolamento do shared.
- Facade para iOS: expõe API clara a SwiftUI sem vazar detalhes de corrotina.
- Plataformas nativas: [[Kotlin]] (Android) e [[SwiftUI|Swift]] (iOS) foram adotados para atender aos requerimentos de apps nativos e, ao mesmo tempo, demonstrar competência prática em [[KMP]] (compartilhando domínio e dados).

## Ferramentas
- Linguagens/UI: [[Kotlin]] (+ Compose Multiplatform/Android), [[SwiftUI]] (iOS).
- Rede/JSON: [[Ktor]] + kotlinx.serialization (multiplataforma, leve, sem reflexão).
- Persistência: [[SQLDelight]] (schema único, queries tipadas, KMP‑friendly).
- Imagem (Android): Kamel (Compose Multiplatform) para carregamento de imagens.
- Build: Gradle (KTS), targets Android/iOS; projetos `shared`, `composeApp`, `iosApp`.
- Testes (planejados): unit tests no domínio e mapeadores; fakes para datasources.

## Organização do desenvolvimento
- Slices verticais: implementar lista → detalhes ponta‑a‑ponta (domínio, dados, UI) para validar arquitetura cedo.
- Contratos primeiro: definir entidades/UseCases/Repo no domínio antes de implementar adapters (evita retrabalho na UI).
- Iterações curtas: começar com mock JSON local (mesmo contrato da API) e trocar para Ktor mantendo o domínio estável.
- Integração contínua local: `:shared:check` e `:composeApp:assembleDebug` para feedback rápido; rodar iOS no Xcode ao final de cada incremento.

## Commits e branches
- Commits pequenos e descritivos: um motivo por commit (ex.: "domain: add CatalogRepository contract", "data: implement SQLDelight schema").
- Mensagens com escopo: prefixos por camada (domain/data/ui/di/docs/chore) para leitura rápida do histórico.
- Sequência lógica: contratos → mocks → adapters reais → UI; cada passo validado por build.
- Branch: trabalho direto em `main` dado o escopo de desafio; em time, usaria feature branches + PRs curtos.

## Fluxo de dados (offline‑first)
- UI → Caso de uso → Repositório → Local (SQLDelight) e, quando disponível, Remote (Ktor).
- Leitura prioritária do cache; refresh coordenado atualiza cache e emite novo estado.
- Imagens: Kamel (Compose Multiplatform) no Android; em iOS a exibição é feita pelo lado SwiftUI.

## Topologia, Atratores e Intensidades (fundamentação conceitual)
- NÃO tentar fundamentar filosoficamente, foco apenas técnico.

## Cobertura dos requisitos
- Lista: título, endereço, rating; toque navega para detalhes.
- Detalhes: título, imagem, descrição, rating; ações “Abrir no Maps” e “Visitar site” em cada plataforma.
- Reutilização: domínio e repositório compartilhados; UI web futura poderia reusar entidades e use cases.

## Como rodar (resumo)
- Gradle sanity: `./gradlew help` e `:shared:check` (gera código do SQLDelight).
- Android: `./gradlew :composeApp:assembleDebug` (ou Android Studio).
- iOS: abrir `iosApp/iosApp.xcodeproj` no Xcode e rodar (opcional `BASE_URL` no Info.plist; mock JSON por padrão).

## Testes e qualidade
- Unidades (planejado/indicados no README): use cases com fakes; mapeadores; validação de `AppResult/DomainError`.
- Contratos estáveis permitem teste determinístico do repositório (fakes de Remote/Local).

## Trade‑offs e próximos passos
- Sem framework de DI no shared: menor over‑engineering; próximo passo poderia ser introduzir Koin/Hilt nos apps.
- Cache TTL/hidratação incremental: ganchos prontos; implementar políticas de expiração/refresh.
- Observabilidade: logs mínimos; adicionar tracing leve e métricas de latência/erros.
- Acessibilidade/UX: melhorias em navegação, foco e tamanhos (Material/iOS Human Interface).

## Perguntas possíveis (e respostas)
- Por que KMP aqui? Para compartilhar domínio/dados e acelerar entrega multi‑plataforma mantendo UI nativa.
- Como lida com erros? `DomainError` mapeia Network/Timeout/NotFound/Unknown; UI exibe estados claros e ações (tentar de novo/abrir offline).
- E se mudar a API? Adapta‑se o adapter remoto/mappers; contratos do domínio permanecem.
- Como trocar mock→API real? Definir `baseUrl` e usar o `HttpClient` real; UI/domínio não mudam.

## Referências rápidas
- Código e decisões: ver README no submódulo.
- [[Desafio Técnico KMP - Requisitos]] · [[Kotlin]] · [[Compose Multiplatform]] · [[SwiftUI]] · [[Ktor]] · [[SQLDelight]] · [[Koin]] · [[MVVM]] (conceito)
