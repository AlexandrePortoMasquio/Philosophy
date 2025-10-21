## Definição

Rotina, em programação, é um bloco nomeado de instruções que pode ser invocado múltiplas vezes ao longo de um programa para resolver uma tarefa específica ou encapsular um cálculo. Subsiste como unidade de decomposição estrutural que mantém isoladas as transformações de dados, favorecendo a reutilização e a clareza do fluxo de controle dentro de um [[Programa]].

## Funcionalidade

A execução de uma rotina implica a criação de um contexto na pilha de chamadas, contendo parâmetros, variáveis locais e o endereço de retorno ao ponto de invocação. A maioria dos ambientes modernos suporta rotinas recursivas, mecanismos de passagem por valor ou referência, além de otimizações como inlining ou tail-call, preservando a coerência do fluxo de instruções sem expor detalhes do hardware.

## Casos de Uso

Rotinas são empregadas na segmentação de tarefas complexas em módulos menores, na implementação de algoritmos compartilhados entre componentes distintos e na definição de interfaces estáveis expostas por bibliotecas. Também sustentam padrões de projeto que dependem de callbacks, manipuladores de eventos e rotinas assíncronas para coordenação de processos concorrentes ou distribuídos.

## Um [[Método (Programação)|método]] é uma rotina?

[[Método (Programação)|Método]] é uma rotina especializada que pertence ao contexto de um tipo, seja uma classe, um objeto ou uma estrutura. Compartilha a natureza de encapsular instruções reutilizáveis, porém acrescenta referências implícitas ao estado da instância e contratos de acesso definidos pelo modelo orientado a objetos.

## Perguntas

* Que critérios determinam a extração de uma nova rotina em sistemas extensos?
* Como equilibrar a divisão entre rotinas puras e rotinas com efeitos colaterais ao projetar camadas de aplicação?
* De que modo convenções de nomenclatura influenciam a leitura de rotinas em equipes distintas?
