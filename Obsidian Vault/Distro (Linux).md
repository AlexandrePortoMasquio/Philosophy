# Distro (Linux)

Relacionado: [[Linux]], [[Sistema Operacional]]

## O que é
Uma distribuição Linux (distro) é um sistema completo que combina o kernel [[Linux]] com um conjunto de softwares de usuário, gerenciador de pacotes, repositórios, instalador e políticas de manutenção. Diferentes distros atendem a públicos e casos de uso distintos (desktop, servidor, embarcado, pesquisa, etc.).

## Como funciona
- Kernel + userland: integrações com bibliotecas, shells, utilitários e serviços.
- Gerenciador de pacotes: instala, atualiza e remove softwares a partir de repositórios assinados.
- Repositórios: conjuntos de pacotes (binários ou fonte) mantidos por equipes e automatizações.
- Modelo de releases: estável (pontos), rolling release ou híbrido (ex.: LTS + intermediárias).
- Init e serviços: normalmente `systemd` hoje; alternativas existem por distro (ex.: OpenRC, runit).

## Principais distribuições
- [[Debian]] — base estável, vasta, foco em software livre.
- [[Ubuntu]] — baseada em Debian, foco em usabilidade e LTS.
- [[Fedora]] — inovação rápida, base upstream do RHEL.
- [[Red Hat Enterprise Linux]] — corporativa, suporte e ciclo longo.
- [[CentOS Stream]] — fluxo contínuo entre Fedora e RHEL.
- [[Arch Linux]] — rolling minimalista, "faça você mesmo".
- [[openSUSE]] — Leap (estável) e Tumbleweed (rolling), YaST/zypper.
- [[Alpine Linux]] — leve, musl+busybox, ideal para containers.
- [[Gentoo]] — baseada em fonte, Portage e USE flags.
- [[NixOS]] — configuração declarativa e reprodutível com Nix.
