---
title: Oráculo (Web3)
updated: 2025-09-16
---
Derivado de [[Web3]]

## Definição

Oráculo, em [[Web3]], é o arranjo que fornece a contratos em [[Blockchain]] dados e eventos que não estão disponíveis on‑chain, ou resultados de computações realizadas fora da cadeia. Atua como ponte entre o ambiente de execução do [[Contrato Inteligente]] e fontes externas, buscando garantir integridade, disponibilidade e previsibilidade de atualização. Diferencia‑se do [[Oráculo (Software)]] (critério de verificação) por operar na camada de fornecimento de fatos ao sistema distribuído.

## Funcionalidade

Funciona por modelos como push (publicação periódica de feeds) ou pull (consulta sob demanda), com validação por assinaturas, agregação de múltiplas fontes e, quando aplicável, provas verificáveis (compromissos, VRF, enclaves, disputas otimistas). Redes de oráculos reduzem pontos únicos de falha ao agregar leituras e aplicar quóruns/limiares; políticas de atualização (janelas, cadência, gatilhos) equilibram custo, latência e frescor. A segurança depende de incentivos criptoeconômicos, diversidade de fontes e mitigação de manipulação/MEV; contingências incluem atrasos, valores limites e rotas de fallback.

## Casos de Uso

Alimentação de preços para finanças descentralizadas, sorteios com aleatoriedade verificável, seguros paramétricos (clima, eventos), execução condicionada por indicadores externos e ponte de resultados de APIs/serviços tradicionais. Exemplo cotidiano: um contrato que liquida posições quando um índice ultrapassa um limiar usa o oráculo para obter o valor de referência com prova e agregação; em caso de falha, aplica limites de segurança e adia a ação até a próxima atualização confiável.

