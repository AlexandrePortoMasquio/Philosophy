---
title: Sealed Class (Kotlin)
tags: [kotlin, tipos algébricos, adt]
created: 2025-08-29
updated: 2025-08-29
---

## Ideia
- Tipo hierárquico fechado: uma `sealed class`/`sealed interface` limita os subtipos diretos ao mesmo arquivo fonte. Permite modelar ADTs (tipos algébricos) com verificação exaustiva em `when`.

## Por que usar
- Segurança de domínio: todos os casos são conhecidos no compile-time; `when` exaustivo dispensa `else` e evita casos não tratados.
- Evolução controlada: adicionar um subtipo falha compilações onde o `when` precisa ser atualizado; evita estados “impossíveis”.

## Exemplos
```kotlin
sealed interface DomainError {
    data object Network: DomainError
    data object Timeout: DomainError
    data class Unknown(val msg: String?): DomainError
}

fun toMessage(e: DomainError) = when (e) {
    DomainError.Network -> "Falha de rede"
    DomainError.Timeout -> "Tempo esgotado"
    is DomainError.Unknown -> e.msg ?: "Erro desconhecido"
}
```

## Notas de linguagem
- Subclasses diretas devem estar no mesmo arquivo (podem ser aninhadas ou top-level). `sealed interface` segue a mesma regra.
- `when` é exaustivo quando cobre todos os subtipos; como expressão, o compilador exige exaustividade.
- Multi-plataforma: funciona em `commonMain` e é útil para modelar estados/resultados compartilhados (usar apenas APIs comuns nos subtipos).

## Ligações
- [[Kotlin]], [[Domain]], [[Padrões de Projeto]] (State, Result), [[Engenharia de Software/Arquitetura de Software|Arquitetura de Software]].

