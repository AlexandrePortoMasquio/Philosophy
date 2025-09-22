[[KMP]]

## Definição

[[Teste Unitário]] verifica, de forma isolada e determinística, pequenas unidades de comportamento (funções ou classes) com execução rápida e resultados reprodutíveis.

Em [[KMP]], prioriza-se o código comum: a lógica de domínio é testada no source set compartilhado; variações de plataforma ficam restritas a pontos `expect/actual` e são exercitadas nos testes de cada alvo.

Em Android, testes locais (JVM) avaliam a lógica sem depender do framework; quando uma API do Android é indispensável, usa-se dublês ou adapta-se o desenho para mover dependências às bordas.

## Princípios

Princípios úteis: um caso de teste deve descrever regra clara (Given–When–Then), focar em um comportamento, controlar tempo e concorrência de modo determinístico e validar o contrato observável. Dependências externas são substituídas por fakes/mocks; efeitos colaterais ficam visíveis por saídas ou interações verificáveis. Métodos privados são cobertos indiretamente pelos públicos; nomes dos testes documentam o requisito que estão garantindo.

## Ferramentas

No código comum, usa-se `kotlin.test` (assertivas e [[Runner]]
integrados), garantindo portabilidade entre alvos. No destino JVM/Android, são correntes JUnit (4/5) para orquestração, MockK para dublês de dependências, e `kotlinx-coroutines-test` para controle de despachantes e avanço de tempo virtual; para fluxos, bibliotecas como Turbine auxiliam na verificação de emissões. No destino iOS/Native, os testes também se baseiam em `kotlin.test`, executados pelo runner nativo.

A execução integra-se ao build: os módulos expõem tarefas de teste por alvo/plataforma; relatórios consolidados registram falhas e coberturas. Quando necessário, configuram-se camadas de interop específicas para permitir testes do código de borda sem acoplar a lógica comum a detalhes de plataforma.

# Teste Unitário
* [[MockK]]
* Testa-se as funções públicas, e as privadas são testadas indiretamente, pois são chamadas pelas públicas
* Não se testa interface, mas sim implementação, que contém a lógica.
* @RelaxedMockK para Mocks de dependências (não serão testadas)
* @InjectMockKs para o subject do teste que recebe as dependências.
* GIVEN (dependência) WHEN (evento) THEN (resultado)
* verifyExactlyOnce(o resultado esperado), verifyNever(o que deve não acontecer no resultado)
