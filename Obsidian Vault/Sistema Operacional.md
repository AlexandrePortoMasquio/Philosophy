

Relacionado: [[Software]] · [[Linux]] · [[Distro (Linux)]] · [[Android]] ······················

## Definição

Camada de software que gerencia recursos do hardware, fornece abstrações (processos, arquivos, memória, rede) e serviços para programas de usuário.

## Como o SO gerencia recursos?

Gerencia por políticas e mecanismos no núcleo e em serviços de sistema: agenda o uso da CPU (escalonamento), aloca e protege memória, organiza o armazenamento em sistemas de arquivos, media entrada e saída por controladores de dispositivo e trata a comunicação de rede. Isola processos, controla privilégios e permissões, contabiliza uso e aplica limites quando definidos. Quando há contenção, arbitra prioridades conforme regras e estado. Exemplo cotidiano: ao abrir muitos aplicativos, processos em segundo plano podem ser suspensos ou encerrados para liberar memória sem afetar o que está em foco.

## Funcionalidade

Oferece abstrações estáveis para que programas interajam com o hardware e entre si: criação e sincronização de processos e threads, acesso a arquivos e rede, relógio e temporizadores, dispositivos e interfaces gráficas, além de serviços de inicialização, atualização, registro e logs. Proporciona multitarefa, segurança (autenticação, autorização, isolamento), conectividade e, em alguns casos, virtualização. Em termos práticos, permite que o mesmo aplicativo opere em máquinas distintas sem conhecer detalhes do dispositivo.

## Exemplos

[[Android]], [[iOS]], [[Linux]], BSD, Windows, macOS.


## Diferenças

Diferem pela arquitetura do núcleo (monolítico, microkernel ou híbrido), pelo modelo de distribuição e licenciamento (livre ou proprietário), pelos mecanismos de atualização e empacotamento, e pelo desenho de interface e políticas de energia. Em dispositivos móveis, prevalecem isolamento rigoroso de aplicativos e restrições a atividades em segundo plano; em desktop e servidores, há maior abertura de configuração e suporte amplo a periféricos. Exemplos: Android prioriza economia de energia e permissões; distribuições Linux variam no gerenciador de pacotes; Windows e macOS integram fortemente interface e drivers.
