
# Operador Lógico

## Operador Lógico Booleano

### Completude Funcional do NOR e NAND

Os operadores [[Lógica Booleana|booleanos]] NOR e NAND são funcionalmente completos (a partir de apenas um deles é possível definir negação, conjunção e disjunção, e assim reconstruir toda a lógica proposicional). Com NAND: ¬p = p NAND p; p ∧ q = ¬(p NAND q) = (p NAND q) NAND (p NAND q); p ∨ q = (p NAND p) NAND (q NAND q). Com NOR: ¬p = p NOR p; p ∨ q = ¬(p NOR q) = (p NOR q) NOR (p NOR q); p ∧ q = (p NOR p) NOR (q NOR q). Na prática, repetir e combinar apenas um desses conectivos basta para expressar qualquer fórmula sem recorrer a outros.

NOR e NAND são os únicos operadores binários individuais que formam um conjunto [[Completude Funcional]] por si sós.




## Relacionar

* [[Lógica]]
* [[Russell]]
* [[Deleuze]]
