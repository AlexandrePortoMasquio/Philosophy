## Requisitos do Contrato Escrow de Cyberia

* O contrato deve ser atualizável via deploy de nova versão durante o MVP, e configurável via parâmetros em storage (ex.: timeout), para evitar imutabilidade absoluta da Solana após deploy inicial.

* Criar escrow descentralizado para tokens CYBERIA.

* As chamadas do contrato deve fazer apenas o Escrow.

* Autorizar-se para usar a conta do consumidor, podendo mover fundos dela.

* Receber um Signed Price Data, assinado pelo provedor, com o preço verdadeiro assinado pelo provedor. O contrato deve conferir se o preço corresponde ao que foi assinado. 

* Caso o contrato tenha autorização para mover fundos da carteira do provedor, permitir um preço negativo para as transações, enviando XCYB do provedor para o consumidor (isto será usado na fase promocional da crypto). A chamada desse tipo de transação promocional poderia ser uma função separada, se essa separação tornar cada chamada mais simples e mais barata. Garantir autorização explícita do provedor (via assinatura ou chamada separada) para mover seus fundos em preços negativos, para manter trustless e evitar riscos de manipulação

* Mover esse valor em tokens da carteira do consumidor para o PDA.

* Segurar esse valor no PDA por 30 segundos.

* Permitir confirmação de entrega bem-sucedida via signed message do consumidor ou provedor, pra manter aberto a qualquer origem e evitar centralização no backend, alinhando com o requerimento de não conhecimento de interface.

* Caso a entrega da resposta da IA seja comunicada como bem-sucedida, entregar o pagamento à carteira do provedor. Caso contrário, devolver ao consumidor.

* O refund deve ser callable por qualquer um após timeout, com verificação on-chain do tempo por Clock.get(), pois ele não pode ser automático na rede Solana.

* Ser minimalista e agnóstico ao conteúdo do prompt.

* Não fazer requisições HTTP.

* Usar token program SPL para transferências.

* Manter taxas baixas na Solana (< 0,01 reais por transação).

* Usar timeout configurável (ex.: 30 segundos).

* Validar apenas mint do CYBERIA.

* O contrato não deveria ter conhecimento da interface ou backend que o chama. Ele deve ser aberto a ser chamado por qualquer origem.

* Ser trustless, sem taxas extras de intermediários. Somente o custo básico em Solana e o preço em CXYB do provedor p2p.

## Endereço do contrato: 
* *github*.com-personal:AlexandrePortoMasquio/cyberia_escrow_contract.git