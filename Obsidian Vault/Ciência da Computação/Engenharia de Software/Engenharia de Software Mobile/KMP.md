---
title: KMP (Kotlin Multiplatform)
tags: [mobile, kotlin, multiplatform]
created: 2025-08-28
updated: 2025-09-15
---
[[Software]]
## Definição
Kotlin Multiplatform (KMP) é um conjunto de capacidades do [[Ecossistema Kotlin]] — suporte do [[Compilador (Kotlin)]], organização por source sets e plugins de build — para compartilhar código entre múltiplas plataformas a partir de uma base comum. Não é uma linguagem nem um framework de interface; trata-se de uma abordagem e de uma ferramenta de compilação/organização de projeto que permite combinar código comum com implementações específicas por plataforma quando necessário. Na prática, o código comum reside em `commonMain` e os trechos específicos em `androidMain` e `iosMain` (mecanismo `expect/actual`).

## Mapa Rápido
- Lado: [[Multiplataforma]] · [[Android]] · [[iOS]]
- Acima: [[Arquitetura de Software]] · [[Linguagem de Programação]]
- Abaixo: [[CI/CD]]

## Ideia
- KMP permite compartilhar código [[Kotlin]] entre [[Android]], iOS e outras plataformas via módulos com `commonMain` (expect) e implementações específicas (`actual`).
- Objetivo: reduzir duplicação de regras de negócio mantendo experiência nativa na [[UI]].
- O [[Compose Multiplatform]] permite também compartilhar a interface de usuário quando conveniente, mantendo integrações nativas nas bordas quando necessário.

## Quando usar
- Domínio com lógica substancial e estável (networking, cache, validação, casos de uso) e UI nativa específica.
- Equipes com proficiência em Kotlin e integração [[iOS]] (Interop Swift/ObjC).

## Vantagens

- Redução de duplicidade: regras de negócio, modelos e políticas residem no módulo compartilhado, diminuindo divergências entre Android e iOS e simplificando manutenção.
- Experiência nativa preservada: UI e integrações ficam nas bordas de cada plataforma, evitando compromissos de desempenho/UX típicos de camadas de abstração de interface.
- Contratos únicos e testáveis: tipos de erro, resultados e validações são definidos uma vez e exercitados por uma suíte comum (`commonTest`), aumentando consistência.
- Entrega coordenada: funcionalidades chegam simultaneamente às plataformas, com menor risco de regressões assimétricas e menor esforço de sincronização entre equipes.
- Dependências sob controle: uso de bibliotecas multiplataforma (Ktor, kotlinx.serialization, SQLDelight) reduz acoplamento a APIs específicas e facilita evolução.

## Prós e Contras em relação ao Flutter

TODO

## Módulos
* [[Domain]]

## Relações Arquiteturais
- Camadas: módulo compartilhado (domínio/dados) e apps finos (UI nativa, DI, navegação).
- Limites claros (API do módulo) preservam modularidade adequada e reduzem acoplamento.
- mapeamentos consistentes (DTOs ↔ modelos de UI), evitando drift entre plataformas.

## Ferramentas
* [[SQDelight]]
* [[Koin]]
* [[Napier]]

## Perguntas e Respostas
- shared vs commonMain: "shared" costuma ser o nome do módulo Gradle; `commonMain` é o source set dentro desse módulo. Padrão de mercado: o source set chama‑se sempre `commonMain`; o nome do módulo varia (ex.: `:shared`, `:core`).

## Tópicos
- Estrutura: [[commonMain]], `androidMain`, `iosMain`; bibliotecas: kotlinx.coroutines, serialization, [[Ktor]].
- Interop iOS: geração de framework, bridging de tipos (nullable, collections), performance de bridging.
- Persistência: multiplataforma (SQLDelight, Realm/KMM) e cache.
- Testes: unitários em comum, instrumentados por plataforma; contratos de API.
- Publicação (MVP): entrega local/README; CI/CD fica para etapas futuras.

## Riscos e Mitigações
- Dissonância de ciclos (Xcode/Gradle): automatizar com scripts e fastlane.
- Supercompartilhamento: manter UI e integrações específicas fora do módulo compartilhado.
- Interop: validar ponte de tipos com suites pequenas de prova.

## Ligações
- [[Multiplataforma]] · [[Android]] · [[iOS]] · [[Engenharia de Software/Processos|Processos]] · [[Engenharia de Software/Ferramentas|Ferramentas]] · [[Arquitetura de Software]] · [[Cyberia Web]]

## Padrões Profissionais (KMP)
- Shared-first: todo Model/Domain/Repository/Data/UseCases ficam em `commonMain` (libs KMP apenas). UI é específica por plataforma.
- HttpClient único (Ktor): instanciado no shared; engines (OkHttp/Darwin) entram só por source sets, sem `expect/actual`.
- SqlDriver por DI: injeção por construtor; drivers (Android/Native) fornecidos nas bordas (Android/iOS), não no shared.
- DI: Koin core no shared (contratos), Koin Android apenas na apresentação Android.
- Resultados: padronizar use cases com `sealed class` para estados/erros (OCP/UX).
- Mappers: explicitar Db→Domain e DTO→Domain (SRP/testes).
- Ports/Adapters: definir interfaces (ports) no domínio (`Repository`, `UseCase`) e manter implementações em data/features; composição via DI nas bordas.

## Por que SQLDelight e Napier no KMP
- SQLDelight: cache offline-first com um único schema/queries no Shared; APIs tipadas geradas a partir de `.sq` evitam erros em runtime; funciona em Android e iOS apenas trocando o driver. Ver [[SQLDelight]].
- Napier: logging multiplataforma (KMP) simples e leve; direciona logs para Logcat no Android e NSLog no iOS; facilita observabilidade mínima sem acoplamento de plataforma. Ver [[Napier]].
