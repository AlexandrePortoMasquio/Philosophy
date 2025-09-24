---
title: Programação Orientada a Objetos
updated: 2025-09-22
---
Derivado de: [[Programação]]
Relacionado a: [[SOLID]]

## Definição

Programação orientada a objetos é um modo de organizar software em torno de objetos: unidades que reúnem estado e comportamento sob um mesmo contrato. O foco recai em encapsulamento (ocultar detalhes e expor intenções), abstração (modelar capacidades relevantes), identidade (objetos distintos podem ter o mesmo valor) e polimorfismo (um mesmo pedido comporta variações de resposta conforme o tipo). Herança é um mecanismo possível de reutilização, mas a prática contemporânea privilegia composição e contratos explícitos.

Não se confunde com “linguagem com classes”: o essencial é projetar colaborações entre objetos que preservem invariantes e tornem as mudanças locais. Avalia‑se pela clareza dos papéis e pela estabilidade dos contratos, não pela quantidade de hierarquias.

## Funcionalidade

Objetos definem invariantes e operações que os mantêm; consumidores interagem por meio de mensagens (métodos), sem acesso direto à representação interna. Contratos explícitos permitem substituir implementações mantendo o comportamento prometido; o polimorfismo evita ramificações por tipo e concentra diferenças onde importam. A inversão de dependência, comum nesse estilo, reduz acoplamento entre quem usa e quem fornece capacidades.

Modelagem orientada a objetos favorece fronteiras claras: cada objeto assume uma responsabilidade coerente; coordenação entre eles compõe casos de uso. Testes exercitam comportamentos observáveis e permitem substituir dependências por dublês, reforçando a verificabilidade.

## Casos de Uso

Adequada quando há entidades com identidade e ciclo de vida, regras que exigem encapsulamento, ou variações de comportamento selecionáveis por contrato (por exemplo, sistemas de domínio ricos, componentes de interface, mecanismos de extensibilidade). Menos indicada para transformações puras e pipelines de dados, onde abordagens funcionais tendem a ser mais diretas. Em arquiteturas mistas, objetos delineiam o núcleo de regras e colaboram com estilos complementares conforme a tarefa.

