# Debian

Relacionado: [[Linux]], [[Sistema Operacional]]

## Visão geral

Debian é uma distribuição de [[Linux]] de propósito geral, conhecida por estabilidade, foco em software livre e um processo de empacotamento rigoroso. Serve de base para dezenas de derivadas (por exemplo, Ubuntu e Kali) e é usada amplamente em servidores, desktops e containers.

## Filosofia e repositórios
- Contrato Social Debian e Diretrizes de Software Livre (DFSG) orientam o projeto.
- Componentes de repositório: `main` (DFSG-livre), `contrib` (requer não-livre) e `non-free` (não-livre). Em versões recentes existe `non-free-firmware` para firmwares distribuíveis.
- Suporte multi-arquitetura: tipicamente `amd64`, `arm64`, `armhf`, `i386`, `ppc64el`, `s390x`, entre outras.

## Ciclo de releases
- Branches: `unstable` (sid), `testing` e `stable` (lançamento atual), além de `oldstable` após novo release.
- Processo de “freeze” congela `testing` até virar `stable`.
- Segurança: atualizações fornecidas por `security` e times LTS/ELTS após EOL.

## Gerenciamento de pacotes
- Baixo nível: `dpkg` instala/remover pacotes `.deb`.
- Alto nível: `apt`/`apt-get`/`apt-cache` para resolver dependências e consultar.
- Arquivos de origem: `/etc/apt/sources.list` e `/etc/apt/sources.list.d/*.list`.
- Exemplo de entrada:
  - `deb http://deb.debian.org/debian stable main contrib non-free non-free-firmware`
  - `deb http://security.debian.org/debian-security stable-security main`
- Pinning e preferências: `/etc/apt/preferences(.d)` para priorizar origens (ex.: backports).

## Comandos úteis (apt)
- Atualizar índices: `sudo apt update`
- Atualizar sistema: `sudo apt upgrade` (ou `sudo apt full-upgrade` para mudanças de dependências)
- Instalar: `sudo apt install <pacote>`
- Buscar: `apt search <termo>` e `apt show <pacote>`

## Sistema e inicialização
- Init padrão: `systemd` na maioria das instalações; alternativas existem (ex.: sysvinit/openrc) via metapacotes.
- Serviços: `systemctl status/start/stop/enable` para gerenciar unidades.
- Alternativas: `update-alternatives` escolhe implementação padrão de ferramentas (ex.: `editor`).

## Estrutura e políticas
- Política Debian define padrões para layout, scripts de manutenção e dependências.
- Patches e metadados mantidos por mantenedores; integração contínua com `autopkgtest` é comum.
- Backports: pacotes mais novos para `stable` com prioridade menor por padrão.

## Identificação do sistema
- Versão: conteúdo de `/etc/debian_version` e `lsb_release -a` (se instalado).
- Kernel: `uname -a`; pacotes do kernel via metapacotes `linux-image-*`.

## Derivadas notáveis
- Ubuntu (desktop/servidor), Linux Mint (desktop), Kali (segurança), Raspbian/Raspberry Pi OS (ARM).

## Quando escolher Debian
- Você prioriza estabilidade, reprodutibilidade e repositórios vastos.
- Precisa de base sólida para servidores ou imagens de container.
- Busca alinhamento com software livre e governança comunitária.
