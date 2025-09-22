---
title: Princípio de Segregação de Interfaces
updated: 2025-09-13
---
[[SOLID]] [[Arquitetura KMP]]
## Definição

O princípio afirma que [[Cliente (Programação)|clientes]] não devem ser obrigados a depender de operações que não utilizam. Em vez de interfaces gerais e inchadas, adotam‑se contratos pequenos, coesos e específicos ao papel de cada consumidor, reduzindo acoplamento, facilitando testes e permitindo evolução sem efeitos colaterais em partes não relacionadas.

## Exemplo

Em KMP, [[UI|UIs]] de `androidMain`/`iosMain` são clientes de contratos definidos em `commonMain`. Em vez de depender de uma interface ampla como `Preferencias` (ler/salvar/limpar/sincronizar), uma tela que apenas consulta um token depende de `LeitorDePreferencias` (por exemplo, `fun token(): String?`), enquanto fluxos de login que gravam usam `EscritorDePreferencias` (por exemplo, `fun salvarToken(...)`).

`LeitorDePreferencias`, neste caso, não é o viewModel, é um contrato de serviço; o [[Cliente (Programação)|cliente]] é o ViewModel que o consome. A cadeia típica mantém interfaces estreitas em cada nível: a view depende apenas de um contrato mínimo do ViewModel (estado e comandos necessários); o ViewModel depende de casos de uso específicos (por exemplo, `ConsultarToken`, `SalvarToken`); cada caso de uso depende de repositórios segmentados (leitor/escritor); e estes dependem de portas de infraestrutura igualmente focadas (APIs/DAO de leitura ou de escrita). Assim, cada componente conhece apenas as operações que efetivamente utiliza, reduzindo acoplamento e evitando efeitos colaterais como gravações ou limpezas indevidas ao executar um fluxo de leitura.

No KMP, os contratos ficam em `commonMain` e as implementações ficam em cada alvo via `actual`. A segregação combinada com esses pontos de variação impede vazamento de detalhes de plataforma, facilita testes com dublês mínimos por papel e permite evoluir implementações sem impactar clientes que não usam as capacidades adicionais.

As implementações `actual` em Android/iOS atendem a cada contrato específico. O acoplamento diminui porque cada cliente conhece apenas o mínimo necessário; reduzem‑se efeitos colaterais como escrita acidental em disco, sincronizações indevidas e limpezas globais. Testes tornam‑se mais simples, com dublês mínimos para cada papel.

## Funcionalidade

Evitar interfaces inchadas: consumidores não devem depender de métodos que não usam. Contratos pequenos e específicos reduzem dependências e permitem implementações focadas.

## Exemplo
Separar “LeituraDeRelatorio” de “EscritaDeRelatorio” evita que clientes de leitura precisem fornecer capacidades de escrita ou tratar erros que não lhes dizem respeito.

## Cuidados e limites
Fragmentação excessiva torna a composição custosa. A segregação deve seguir fluxos reais de uso e pontos de estabilidade do domínio.

## Alguma leitura de documentação recomendada?

Útil manter: (a) guia de design de interfaces com foco em [[Contrato (Software)|contratos]] mínimos por [[Cliente (Programação)|cliente]], separação leitura/escrita, pré/pós‑condições e erros (ver “Interface Segregation Principle”: https://pt.wikipedia.org/wiki/Princ%C3%ADpio_da_segrega%C3%A7%C3%A3o_de_interface); (b) orientação [[Desenvolvimento KMP]] para `expect/actual` e organização de `commonMain` versus alvos, com exemplos de adaptação por plataforma (Kotlin Multiplatform — expected/actual: https://kotlinlang.org/docs/multiplatform-connect-to-apis.html); (c) template de [[Teste Unitário (KMP e Android)|testes de contrato]] (Given–When–Then) para verificar que implementações distintas preservam o mesmo comportamento sob a interface (Contract tests: https://martinfowler.com/bliki/ContractTest.html; Gherkin: https://cucumber.io/docs/gherkin/reference/).

## Relações
[[SOLID]] · [[Desenvolvimento de Software]] · [[Software]]
