---
title: Microsserviço
updated: 2025-09-16
---
[[Desenvolvimento de Software]]
## Definição

Microsserviço é um serviço pequeno e autônomo, delimitado por uma responsabilidade clara, com dados e implantação próprios, que colabora com outros serviços em uma arquitetura distribuída. A identidade do serviço é dada por seu [[Contrato (Software)|contrato]] estável (operações e formatos), não por tecnologias internas. Difere de um monólito modular por permitir evolução e implantação independentes, ao custo adicional de coordenação em [[Sistemas Distribuídos]].

## Funcionalidade

Cada serviço expõe uma API síncrona (por exemplo, [[HTTP]]/gRPC) e/ou reage a mensagens assíncronas (filas/eventos), mantendo seu armazenamento privado. A comunicação entre serviços requer versionamento compatível, tolerância a falhas (timeouts, retrocessos) e observabilidade suficiente para diagnosticar dependências. Em [[Arquitetura de Software]], a decomposição costuma seguir limites de domínio; contratos precisos e testes de contrato preservam estabilidade mesmo com mudanças internas. Bibliotecas e detalhes técnicos são intercambiáveis desde que o contrato permaneça íntegro.

## Casos de Uso

Adequado quando partes do sistema evoluem em ritmos distintos, quando há necessidade de escalar seletivamente funções específicas ou quando equipes autônomas trabalham em fronteiras bem definidas. Exemplos: pagamentos, catálogo e recomendações como serviços separados em um comércio eletrônico. Riscos incluem complexidade operacional, latências de rede e consistência distribuída; quando o domínio é pequeno e a equipe é reduzida, um monólito modular pode oferecer melhor relação custo–benefício.
