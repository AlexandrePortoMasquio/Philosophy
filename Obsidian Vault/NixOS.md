# NixOS

Relacionado: [[Distro (Linux)]], [[Linux]]

## O que é
Distro que usa o gerenciador Nix para empacotamento e configuração declarativa do sistema, com foco em reprodutibilidade.

## Como funciona
- `nix` e `nixos-rebuild` aplicam uma configuração (normalmente `configuration.nix`) que descreve todo o sistema.
- Deploys atômicos, múltiplas gerações e rollback fácil; isolamento de dependências por store imutável.
