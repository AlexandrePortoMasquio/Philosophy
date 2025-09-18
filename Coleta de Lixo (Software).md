---
title: Coleta de Lixo (Software)
updated: 2025-09-16
---
Derivado de [[Memória (Software)]]

## Definição

Coleta de lixo é a estratégia de gerenciamento automático de [[Memória (Software)]] que identifica e libera [[Espaço de Memória|regiões]] que se tornaram inacessíveis para o programa, evitando vazamentos, uso‑após‑liberação e dupla liberação. Em vez de o código aplicar liberações manuais, um coletor rastreia referências a partir de raízes (pilhas, registros, objetos estáticos) e determina quais objetos permanecem alcançáveis; os demais podem ser recuperados. O objetivo é equilibrar segurança e desempenho, reduzindo erros de gerenciamento de memória ao custo de tempo de coleta e alguma sobrecarga.

## Funcionalidade

Coletores operam, em geral, por marcação e varredura (marcar objetos alcançáveis e varrer os demais), cópia (mover vivos para uma área e liberar o restante) ou esquemas geracionais que separam jovens e antigos, explorando o padrão de “a maioria dos objetos morre jovem”. Variantes incrementais e concorrentes reduzem pausas ao repartir o trabalho, enquanto compactação reorganiza o heap para diminuir fragmentação. Barreiras de escrita/leitura mantêm a visão do coletor coerente com a execução concorrente. Em ambientes como a [[JVM]], políticas ajustáveis (gatilhos, tamanhos, metas de pausa) permitem adaptar o coletor ao perfil de carga, trocando latência por throughput conforme o caso.

## Casos de Uso

Aplicações servidoras e de longa duração se beneficiam de coleta de lixo pela redução de classes de erro e pela estabilidade de execução sob evolução contínua; ajustes de heap e metas de pausa alinhados ao SLA evitam caudas de latência. Em [[Android]], pausas do coletor podem afetar fluidez de UI; reduzir alocações no caminho quente, reutilizar buffers e limitar picos de criação de objetos diminuem a pressão no heap e as pausas visíveis (ver [[Perfetto]] para identificar engasgos ligados a GC e [[Coleta de Lixo (Android)]] para detalhes da plataforma). Em projetos [[KMP]], diferenças de runtime entre alvos recomendam atenção à fronteira de dados e à orquestração de alocações; ver [[Coleta de Lixo (KMP)]]. Em bibliotecas e módulos compartilhados, projetar APIs que evitem cópias desnecessárias e grafos grandes reduz custos indiretos sem abrir mão da segurança.

## Ver também
[[Coleta de Lixo (Android)]] · [[Coleta de Lixo (KMP)]] · [[JVM]] · [[Android]]
