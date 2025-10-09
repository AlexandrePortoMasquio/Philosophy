Relacionado: [[Linux]] · [[Android]] · [[Sistema Operacional]]

## Definição

SELinux é um mecanismo de controle de acesso obrigatório no kernel Linux que aplica políticas de segurança por rótulos a processos e objetos (arquivos, [[Socket (Programação)|sockets]], dispositivos). A política define, com negação por padrão, quais interações são permitidas entre domínios, independentemente das permissões discricionárias do sistema de arquivos. O resultado é isolamento mais fino entre componentes, redução da superfície de ataque e limitação do impacto de comprometimentos.

## Estrutura

Baseia‑se em rótulos (contextos) atribuídos a processos e objetos e em uma política que define quais domínios (tipos) podem executar quais operações sobre quais tipos de objeto. Os contextos seguem a forma usuário:papel:tipo:nível; na prática, o controle principal decorre do tipo (TE), com extensões por papéis (RBAC) e por níveis/categorias (MLS/MCS) quando habilitadas. O kernel intercepta chamadas por ganchos de segurança, consulta o cache de decisões (AVC) e aplica a regra correspondente; mapeamentos de rótulos para o sistema de arquivos (file contexts) e booleanos da política permitem ajustes controlados sem reescrever a política. Exemplo: um servidor web no domínio httpd_t lê apenas conteúdo rotulado como httpd_sys_content_t, sendo bloqueado ao tentar acessar diretórios não rotulados para esse serviço.

## Como se aplica ao Android

No Android, SELinux opera em modo de imposição para restringir serviços do sistema e aplicativos a domínios específicos, de modo que cada processo só executa operações explicitamente autorizadas (por exemplo, um app de mídia não pode ler bancos de dados de outro app). A política base do sistema, combinada com ajustes do fabricante, controla acesso a dispositivos, arquivos e interfaces de comunicação (como o Binder), registra violações e bloqueia ações não previstas. Em termos práticos, mesmo que uma vulnerabilidade permita a execução de código, o domínio do processo impede que esse código alcance dados e recursos de outros componentes sem permissão definida.
