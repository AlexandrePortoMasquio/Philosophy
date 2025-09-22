---
title: Princípio de Substituição de Liskov
updated: 2025-09-13
---
[[SOLID]]
## Definição

Definição do LSP: O princípio da substituição de Liskov, proposto por Barbara Liskov, afirma que, se uma classe S é um subtipo de uma classe T, então objetos do tipo T podem ser substituídos por objetos do tipo S sem alterar o comportamento esperado do programa. Em outras palavras, uma instância de uma classe derivada (subclasse) deve ser capaz de substituir uma instância de sua classe base (superclasse) sem quebrar a lógica ou as expectativas do sistema.

O princípio de substituição de Liskov afirma que tipos derivados devem poder substituir seus básicos sem violar promessas observáveis. Pré‑condições não podem ser fortalecidas, e pós‑condições e invariantes não podem ser afrouxados de modo a quebrar usos válidos previstos pelo contrato.

## Exemplo

Se “Pagamento” promete lançar exceções específicas e registrar auditoria, implementações derivadas devem manter essas garantias. Acrescentar requisitos extras de estado ou suprimir registros viola a substituibilidade.

## Substituição de Liskov e Polimorfismo

Polimorfismo permite usar implementações distintas por meio de um mesmo contrato. A substituição de Liskov explicita a condição para que tal uso seja seguro: compatibilidade comportamental, não apenas de assinatura. Um tipo substituto deve aceitar pelo menos os mesmos estados válidos (não fortalecer pré‑condições), garantir no mínimo os mesmos efeitos e pós‑condições prometidos e preservar invariantes relevantes. Quando isso falha, a variedade de implementações degrada em surpresa para o cliente, anulando a generalidade pretendida.

Em termos práticos, contratos claros delimitam entradas válidas, efeitos e erros previstos; testes de contrato exercem a mesma suíte sobre cada implementação para verificar substituibilidade. Restrições adicionais ou efeitos omitidos indicam que o contrato base é estreito ou impreciso e deve ser revisado, ou que se trata de um caso para composição em vez de herança. Ver [[Contrato (Software)]] e [[Precisificação]].

## Combinando Polimorfismo com Substituição de Liskov no Android e KMP

Exemplo: há uma classe base “Conta” com a função “pegarEmpréstimo”, e deseja‑se uma derivada “ContaFuncionário” que não pode pegar empréstimo. Para preservar Liskov e o polimorfismo, o contrato da operação deve permitir negação como resultado válido, e não exigir que toda conta aprove. Reformule a operação como “solicitarEmpréstimo(valor): Resultado”, onde Resultado especifica “Aprovado” ou “Negado (motivo)”, com invariantes claros. “ContaFuncionário” pode sempre retornar “Negado” mantendo o mesmo contrato e sem lançar exceções inesperadas ou impor pré‑condições adicionais; clientes que trabalham via “Conta” continuam corretos. Alternativamente, segregue a capacidade: declare uma interface “ContaComEmpréstimo” com “solicitarEmpréstimo”; apenas contas habilitadas a implementam, e consumidores que exigem empréstimo dependem desse contrato específico (ver [[Princípio de Segregação de Interfaces]]).

Em KMP/Android, defina o contrato em `commonMain` e garanta que todas as implementações (incluindo “ContaFuncionário”) preservem as mesmas pré‑ e pós‑condições: a chamada sempre retorna um Resultado consistente, com tempos e erros previstos; diferenças de ambiente (permissões, threads, persistência) são encapsuladas sem alterar a semântica. Testes de contrato aplicados a várias contas (com e sem empréstimo) verificam que clientes polimórficos não quebram: quem precisa apenas de “Conta” não assume aprovação; quem precisa de empréstimo seleciona “ContaComEmpréstimo”. Quando a necessidade nega o contrato base, prefira composição ou segregação a herança, evitando violar substituibilidade.

## Relações
[[SOLID]] · [[Teste Unitário]]
