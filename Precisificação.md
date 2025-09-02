---
title: Precisificação
tags: [vagueza, semântica, metodologia, informação]
created: 2025-09-01
updated: 2025-09-01
---

## Conceito
- Precisificação: operação que torna mais determinado um predicado/termo vago, fixando critérios sob um código/contexto/finalidade. Não revela uma essência; seleciona um recorte operacional do [[Campo Conceitual]].
- Família admissível: em vez de uma única resposta, há um conjunto de precisificações que respeitam casos claros e variam nas bordas (ver [[Supervaloração]]). A escolha depende de custos/objetivos (previsão, justiça, controle, explicação).
- Interface com o [[Princípio de Vagueza]]: toda precisificação herda certo borrão residual e pode exibir [[Vagueza de Ordem Superior]]; seu papel é gerir, não eliminar, a vagueza.

## Operação (esboço)
- Entradas: propósito F, domínio D, código/modelo C, tolerância de erro ε, casos claros S_claros.
- Saída: predicado P_C,F: D → {0,1} (ou valor graduado em [[Fuzzy]]) com fronteiras e justificativas explícitas.
- Passos:
  1) Fixar invariantes: o que deve permanecer (núcleo do uso; [[Invariantes]]).
  2) Eleger métricas: distância/relevância no domínio (custo de erro, risco, fairness etc.).
  3) Propor cortes: thresholds, regras, ou parâmetros do código C.
  4) Testar robustez: variação sob reparametrizações equivalentes (ver “admissibilidade”).
  5) Reportar curvatura: documentar [[Curvatura]] (ordem de critérios, escala) e sensibilidade.

## Tipos de Precisificação
- Supervaloração: conjunto de precisificações admissíveis; “super‑verdade” = verdade em todas; preserva muito da lógica clássica; lida bem com casos claros; pressiona em [[Vagueza de Ordem Superior]].
- Fuzzy: μ: D→[0,1]; captura gradualidade e decisão sob risco; requer escolhas (t‑normas, thresholds) documentadas.
- Contextualista: padrões mudam com finalidade/atividade; útil para diálogo e direito; precisa fixar contexto para séries de [[Sorites]].
- Paramétrica: cortes numéricos (ex.: “alto” ≥ θ); simples, auditável; risco de arbitrariedade se θ não for calibrado ao custo.
- Baseada em modelo: ampliar o código C (features, regras) para reduzir ruído e deslocar bordas mantendo o núcleo (aumenta [[Ordem Informacional]] relativa ao domínio).

## Admissibilidade (critérios)
- Respeito a casos claros: conservar avaliações pacíficas do uso ordinário/experto.
- Coerência com invariantes: preservar o papel operacional do conceito (núcleo funcional).
- Robustez multi‑código: variações pequenas de reparametrização não devem inverter maciçamente casos.
- Parcimônia: complexidade mínima para igual desempenho preditivo/operacional (compressão em [[Informação]]).
- Transparência: cortes/racional justificáveis e auditáveis.

## Métricas úteis
- Distância de extensões: Jaccard/simetria de conjuntos entre precisificações candidatas.
- Erro e utilidade: curvas ROC/PR, custo esperado, valor de decisão.
- Informação: variação de entropia condicional e informação mútua sob o código C.
- Espessura de borda: largura da zona de desacordo entre precisificações admissíveis.
- Curvatura: divergência entre caminhos de atualização (ordem de filtros/escala) no [[Campo Conceitual]].

## Exemplos
- Direito (“razoável”): fixar standards por precedentes vs por custo social; comparar bordas e espessura residual.
- Biologia (“espécie”): morfologia→genética vs genética→ecologia; núcleos estáveis + separatrizes móveis.
- Cotidiano (“alto/rico”): thresholds calibrados por risco/objetivo; relatar sensibilidade e fairness.

## Relações
- [[Vagueza]] · [[Princípio de Vagueza]] · [[Vagueza de Ordem Superior]] · [[Supervaloração]] · [[Fuzzy]] · [[Contextualismo]]
- [[Campo Conceitual]] · [[Curvatura]] · [[Informação]] · [[Ordem Informacional]] · [[Invariantes]] · [[Atratores]] · [[Atualização]] · [[Virtualidade]] · [[Vacuidade]]

## Perguntas Abertas
- Quando preferir família de precisificações (relato de incerteza) versus fixar um corte único (decisão)?
- Como balancear parcimônia com justiça/robustez em domínios sensíveis (direito, políticas públicas)?
- Medidas padrão para “espessura de borda” e “curvatura” comparáveis entre domínios distintos.

## Mapa Rápido
- [[Supervaloração]] · [[Fuzzy]] · [[Contextualismo]] · [[Campo Conceitual]] · [[Curvatura]]

