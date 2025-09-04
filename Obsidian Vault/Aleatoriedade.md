---
title: Aleatoriedade
tags: [aleatoriedade, informação, probabilidade]
created: 2025-09-04
updated: 2025-09-04
---
# Aleatoriedade

- Ausência de padrão útil relativa a um [[Código]]/modelo: o que não é capturado nem previsto ("[[Ruído]]") pelo código vigente é percebido como aleatório.
- Três intuições equivalentes, sob condições: imprevisibilidade (não antecipável), incompressibilidade (não resumível) e equiprovabilidade (distribuição máxima de incerteza dada as restrições).
- Na [[Cosmologia Informacional]], aleatoriedade é saldo de variação não codificada em processos que atualizam a [[Virtualidade]]; conecta-se à [[Entropia Informacional]].

## Perspectivas
- Estatística (Shannon): aleatório = alta incerteza H; para variáveis discretas com suporte finito e sem restrições, o máximo é a distribuição uniforme.
- Algorítmica (Kolmogorov‑Chaitin): aleatório = incompressível; um objeto é aleatório se não admite descrição significativamente menor que ele mesmo (ver [[Complexidade de Kolmogorov]]); testes de [[Compressão]] aproximam.
- Epistêmica vs Ontológica: imprevisibilidade por ignorância/modelo limitado vs indeterminação física (ex.: fenômenos quânticos). Em prática, tratamos como relativa ao código/observador.

## Independência de utilidade
- Aleatoriedade não depende de [[Utilidade]]: define-se por incerteza/compressibilidade relativas a um código, não por valor ou finalidade.
- Encadeamento ontológico: [[Entropia Informacional]] fundamenta a seta do [[Espaço-Tempo|tempo]]; utilidade depende do tempo (decisão/processo), logo utilidade não pode fundamentar entropia nem aleatoriedade.

## Formalizações (curtas)
- [[Shannon]]: H(X) mede incerteza; H(Y|X) mede ruído relativo a X; I(X;Y) mede sinal (redução de incerteza pela correlação).
- Kolmogorov: K(s) aproxima a aleatoriedade algorítmica de s; strings pouco compressíveis têm alta aleatoriedade.
- Testes de aleatoriedade avaliam hipóteses estatísticas (uniformidade, independência, autocorrelação, runs); não “provam” aleatoriedade, apenas rejeitam padrões.

## Fontes e Geração
- Físicas: ruído térmico, tempo de decaimento radioativo, jitter de oscilador, fotões em divisores de feixe (quantum).
- Computacionais: PRNG (determinísticos, ex.: Mersenne Twister, Xoshiro) vs CSPRNG (criptograficamente seguros, ex.: ChaCha20, AES‑CTR, /dev/urandom). Semeadura (seed) precisa de entropia do sistema.
- Mistura/condensação: pools de entropia, hashing/KDF (ex.: HKDF) para derivar chaves a partir de fontes brutas.

## Testes e Critérios
- Baterias: NIST SP 800‑22, Dieharder, TestU01; cobrem frequência, blocos, runs, espectral, compressibilidade, etc.
- Limitações: passar testes não garante aleatoriedade universal; falhar revela padrão explorável. Use múltiplos testes e volumes adequados.

## Boas práticas (engenharia)
- Use CSPRNG para [[Criptografia]]; nunca use PRNG não seguro para chaves/salts/IVs.
- Cuide da seed: coletores de entropia reais; não reutilize seeds previsíveis; derive por KDF.
- Para [[Simulação]]/Monte Carlo, foque em qualidade estatística (periodicidade, correlações) e reprodutibilidade (seed fixo documentado).
- Monitore fontes de entropia em produção; isole determinismo onde necessário para testes, injetando aleatoriedade por portas/abstrações.

## Armadilhas comuns
- Confundir “parecer aleatório” visualmente com testes formais.
- Assumir que alta H implica segurança: entropia observável não implica imprevisibilidade computacional sem CSPRNG.
- Tomar ruído de sensor sem des‑biasing; ignorar vieses e correlações temporais.

## Ligações
- Conceitos: [[Informação]], [[Entropia Informacional]], [[Compressão]], [[Complexidade de Kolmogorov]], [[Código]], [[Ruído]], [[Computação]].
- Métodos: [[Probabilidade]], [[Estatística]], [[Aprendizado de Máquina]] (ruído/regularização), [[Simulação]].
- Sistemas: [[Criptografia]], [[Controle]] e [[Lei da Variedade Requisitada]] (variedade/ruído vs capacidade de discriminação).

## Referências rápidas
- NIST SP 800‑90 (geração de números aleatórios), SP 800‑22 (testes).
- Lições clássicas: Shannon (entropia), Kolmogorov/Chaitin (aleatoriedade algorítmica), Martin‑Löf (testes universais).
