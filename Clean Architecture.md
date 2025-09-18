---
title: Clean Architecture
updated: 2025-09-14
---
 [[Arquitetura de Software]]
## Definição

Clean Architecture é um padrão de design que organiza o sistema de modo que as regras de negócio permaneçam independentes de dispositivos (hardware, sistemas operacionais e recursos de plataforma), interfaces e [[Persistência (Software)|mecanismos de persistência]] (bancos de dados, arquivos e caches). As dependências apontam para dentro: políticas de alto nível não dependem de detalhes de implementação. Exemplo cotidiano: a política de trocas de uma loja não deve depender do modelo da maquineta de cartão; pode-se trocar o equipamento sem reescrever a regra.

## Por que importa

Esse arranjo torna o núcleo do domínio mais claro e testável, facilita a substituição de detalhes (bancos de dados, bibliotecas de rede, camadas de apresentação) e reduz o custo de mudança ao longo do tempo. Ao separar políticas estáveis de meios voláteis, aumenta-se a longevidade do sistema e diminui-se o acoplamento acidental entre partes que evoluem por razões distintas.

## Cuidados e limites

Excesso de camadas e abstrações prematuras introduz indireções desnecessárias e dificulta a leitura. Fronteiras devem acompanhar invariantes do domínio e ritmos reais de mudança; generalizações só valem quando há variação concreta a acomodar. Dogmatismo na separação pode paralisar a entrega; pragmatismo guiado pelo domínio preserva a coesão sem burocracia.

## Relações
[[Desenvolvimento de Software]] · [[Princípio de Inversão de Dependência]] · [[Precisificação]] · [[SOLID]]
