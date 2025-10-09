Relacionado: [[Sistema Operacional]] · [[Linux]] · [[Computação]]

## Definição

Socket é a abstração do sistema operacional para um ponto de comunicação entre processos, local ou em rede. Representa um endpoint identificado por uma família de endereços (por exemplo, Internet ou Unix), um tipo de comunicação (fluxo orientado a conexão ou datagrama) e, quando aplicável, um protocolo. Apresenta‑se como descritor de arquivo, de modo que leitura e escrita seguem chamadas padronizadas, com controle de permissões e isolamento providos pelo sistema.

## Funcionalidade

Permite estabelecer conexões (cliente) ou aceitar conexões (servidor), enviar e receber dados, configurar tempos de espera e modos de operação (bloqueante ou não bloqueante) e selecionar interfaces e portas. Em nível local, viabiliza comunicação entre processos no mesmo sistema; em rede, interage com a pilha de protocolos para endereçar hosts e rotear pacotes. A multiplexação por eventos possibilita atender muitos sockets de forma eficiente, enquanto políticas do sistema definem limites e prioridades.

## Casos de Uso

Servidores web e bancos de dados escutam sockets para atender requisições; aplicativos de mensagens mantêm sockets para receber notificações e trocar conteúdo em tempo real; sistemas distribuídos coordenam nós por sockets para replicação e consenso; no ambiente local, sockets Unix conectam serviços e ferramentas sem passar pela rede externa. Exemplo cotidiano: ao abrir um mensageiro, a aplicação cria uma conexão persistente para receber novas mensagens sem precisar consultar o servidor a cada instante.

