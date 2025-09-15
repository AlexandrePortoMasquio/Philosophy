---
title: Multiparadigma
updated: 2025-09-14
---
"Multiparadigma" designa a capacidade de uma [[Linguagem de Programação]] ou [[Arquitetura de Software]] acomodar estilos distintos de construção de software ([[Programação Imperativa]], funcional, orientado a objetos, declarativo), escolhendo o instrumento mais adequado a cada parte do problema. O objetivo é aumentar a expressividade sem aprisionar o projeto a um único modo de raciocínio. Exemplo cotidiano: uma mesma cozinha usa panela de pressão, forno e frigideira conforme a preparação; nenhuma ferramenta basta para tudo.

## Por que importa

Permite combinar vantagens de paradigmas diferentes: imutabilidade e composição funcional para lógica de transformação; encapsulamento e tipos algébricos para modelagem; efeitos controlados para entrada e saída. Essa flexibilidade costuma reduzir acoplamento acidental e tornar intenções mais transparentes, desde que as fronteiras entre estilos sejam nítidas e guiadas pelo domínio.

## Cuidados e limites

Ecletismo sem critérios produz colagem incoerente e dificulta manutenção. Convém definir princípios de uso por contexto (onde mutação é aceitável, onde composição pura é preferível) e manter consistência no interior de cada módulo. Generalização excessiva e camadas desnecessárias são sinais de desvio; simplicidade local e coesão devem prevalecer sobre exibicionismo técnico.

## Relações
[[Kotlin]] · [[Desenvolvimento de Software]] · [[Clean Architecture]] · [[Princípio de Responsabilidade Única]]

