---
title: Memória (Software)
updated: 2025-09-15
---
[[Software]]
## Definição

Em [[Software]], a memória é o espaço de [[Endereçamento (Software)]] disponível para um processo [[Armazenamento (Software)|armazenar]] e recuperar [[Dados (Software)]] temporários durante a execução. Inclui regiões com papéis distintos (código, dados estáticos, pilha e heap) e obedece a políticas do [[Kernel (Software)]] e do runtime (alocadores, coleta de lixo, verificações). Diferencia‑se de [[Persistência (Software)]] por não visar conservação durável: seu conteúdo pode ser descartado ao término do processo ou por pressão do sistema.

## Memória é o mesmo que Armazenamento?

Não. A memória é volátil e orientada à execução imediata: guarda estados de trabalho do processo com acesso de baixa latência e perde o conteúdo ao fim do processo ou por falta de energia/pressão do sistema. [[Armazenamento (Software)]] ([[Disco (Software)]]/[[SSD]]/flash) visa conservação durável sob latências maiores, organizado por sistemas de arquivos ou bancos de dados. Enquanto a memória sustenta cálculos em andamento, o armazenamento preserva resultados e registros ao longo do tempo.

Exemplo: ao redigir um texto, caracteres digitados residem na memória do editor e podem ser perdidos em um encerramento abrupto; ao salvar, o conteúdo é gravado no [[Armazenamento (Software)]] e permanece disponível após reinicializações. Trocas automáticas (swap/paging) podem mover páginas entre memória e armazenamento como técnica de gestão, mas não alteram a distinção funcional entre execução volátil e conservação durável.

## Funcionalidade

A memória sustenta estados intermediários de cálculos, estruturas de dados e buffers de I/O, condicionando desempenho e segurança. O sistema operacional isola espaços de processo e fornece páginas sob demanda; o runtime organiza alocação, desalocação e, quando aplicável, coleta de lixo. Localidade espacial e temporal orienta a disposição eficiente de dados; modelos de memória e sincronização determinam visibilidade entre threads, tornando relevante a atenção a concorrência e [[Thread Safety]].

## Casos de Uso

Aplicações com grandes coleções (listas, mapas), processamento de mídia e redes exigem gestão cuidadosa de footprint e de cópias para evitar pausas e encerramentos por falta de memória. Exemplo cotidiano: ao abrir uma galeria com milhares de fotos, carregar miniaturas sob demanda e reutilizar buffers evita picos de uso; em mobile, o sistema pode encerrar processos que excedem limites. Boas práticas incluem reduzir alocações no caminho quente, reciclar objetos e preferir estruturas adequadas ao padrão de acesso.

## Em Android e KMP

Em [[Android]], o gerenciamento de memória ocorre sob a ART com coleta de lixo e limites por classe de memória. O app deve minimizar alocações na thread principal, controlar o ciclo de vida de bitmaps/buffers e responder a sinais do sistema (por exemplo, callbacks de trim) reduzindo caches. Fugas de referência e objetos estáticos excessivos degradam a estabilidade; medir e observar padrões de alocação orienta correções que preservam fluidez.

Em [[KMP]], o código comum modela estruturas e fluxos, enquanto detalhes de alocação e representações podem variar entre JVM e Native. Ao cruzar fronteiras (Android↔shared, iOS↔shared), evitar grafos grandes e cópias desnecessárias; preferir modelos de dados estáveis e conversões explícitas nas bordas. Em cenários sensíveis, medições orientam simplificações de dados e redução de picos, mantendo o domínio desacoplado de decisões específicas de runtime.
