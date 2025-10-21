## Definição

Método em programação designa uma rotina associada a um tipo, responsável por operar sobre dados encapsulados ou representar comportamentos previstos por uma classe, objeto ou estrutura. Funciona como contrato formal para manipular o estado interno, distinguindo-se de uma [[Rotina (Programação)]] genérica por carregar contexto implícito, como a referência à instância ou ao protótipo em que reside.

## Qual a diferença entre método e função?

Função é uma rotina independente que pode ser invocada sem vínculo obrigatório a um tipo ou instância, recebendo explicitamente todos os dados necessários para executar sua lógica, ainda que linguagens orientadas a objetos permitam funções globais ou associadas a módulos estáticos. Método, ao contrário, carrega um receptor implícito e opera sobre o estado protegido do tipo ao qual pertence, obedecendo regras de visibilidade, herança e despacho dinâmico que não são requisitos estruturais para uma função livre.

## Funcionalidade

Cada invocação de método constrói um quadro de pilha que inclui a instância receptora (`this` ou `self`), os parâmetros declarados e o espaço para variáveis locais, permitindo acesso direto aos campos protegidos pelo tipo. Métodos podem ser estáticos ou virtuais, podem participar de sobrecarga e sobrescrita, e recorrem a mecanismos de despacho dinâmico para selecionar a implementação apropriada em hierarquias de herança ou composição, preservando a integridade dos invariantes do tipo.

## Casos de Uso

Interfaces orientadas a objetos dependem de métodos para expor operações idempotentes e mutáveis sobre o estado interno, harmonizando encapsulamento e extensão. Padrões como Strategy, Template Method e Observer estruturam comportamentos intercambiáveis por meio de métodos polimórficos, enquanto APIs de serviços utilizam métodos estáticos para oferecer fábricas, validadores e adaptadores coerentes com o ciclo de vida de componentes.
