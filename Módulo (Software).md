---
title: Módulo (Software)
updated: 2025-09-16
---
Derivado de [[Software]]

## Definição

Módulo é uma unidade coesa de organização de informação e de empacotamento que estabelece fronteiras técnicas claras: o que é exposto (interface pública) e o que permanece interno ([[Implementação (Software)]]). Um módulo compila e evolui de modo relativamente independente, declara dependências explícitas e publica uma superfície estável de uso ([[API]]), reduzindo acoplamento e favorecendo substituição e testes. Distingue‑se de “componente” pelo foco na unidade de build/empacotamento e de “pacote” pelo foco em nomenclatura e organização interna.

## Funcionalidade

Os módulos separam contratos de realização: a interface define operações e tipos; a implementação pode variar sem afetar consumidores, desde que o contrato permaneça. Essa separação viabiliza inversão de dependências e arquiteturas em camadas: regras de negócio dependem de [[Contrato (Software)|contratos]], não de detalhes concretos, e detalhes são ligados nas bordas conforme o contexto (ver [[Clean Architecture]] e [[Princípio de Inversão de Dependência]]). A visibilidade controlada (público/interno), a compilação incremental e o versionamento tornam mudanças localizadas mais seguras e auditáveis.

## Casos de Uso

Separar domínio de dados em aplicações: um módulo com entidades e casos de uso expõe contratos, enquanto outro fornece repositórios e integrações; trocar a fonte de dados não exige alterar o domínio. Organizar funcionalidades por área (ex.: “catálogo” e “pagamentos”) para que equipes trabalhem com autonomia e testes direcionados. Publicar bibliotecas reutilizáveis com interface estável e implementação evolutiva. Exemplo cotidiano: um serviço de pagamento permanece o mesmo para a aplicação mesmo que a provedora mude; como o módulo expõe o contrato, apenas sua implementação concreta é substituída.

## No SOLID

Em nível de módulo, os princípios de [[SOLID]] orientam recorte, superfície e dependências. Responsabilidade única delimita uma razão de mudança coesa (função de domínio, camada ou capacidade). Aberto/Fechado recomenda que variações entrem por extensão (pontos de variação explícitos, estratégias, eventos), preservando o contrato estável. Substituição de Liskov exige que implementações e versões novas mantenham as promessas observáveis do módulo; precondições não se fortalecem, pós‑condições não se enfraquecem. Segregação de Interfaces incentiva APIs pequenas e específicas por consumidor, evitando dependências desnecessárias. Inversão de Dependência direciona o acoplamento para abstrações estáveis do próprio módulo, com detalhes compostos nas bordas.

Aplicação prudente requer declarar contratos e invariantes, isolar pontos de variação e evitar indireções supérfluas. Recortes artificiais degradam legibilidade; falta de coesão acumula motivos distintos de mudança. O módulo bem recortado equilibra extensão e estabilidade: contratos claros, dependências explícitas e evolução local verificável. Ver também [[SOLID]].
