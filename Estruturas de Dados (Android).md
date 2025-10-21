## Definição

Estruturas de dados em Android consistem na organização de coleções de valores dentro da heap administrada pela [[Runtime]] Dalvik ou ART, utilizando as bibliotecas padrão de Java e Kotlin. Servem para garantir acesso eficiente a sequências, conjuntos e associações, sustentando a manipulação de estados persistentes ou transitórios em aplicações móveis.

## Funcionalidade

Arrays (`T[]` em [[Java]] e `Array<T>` em [[Kotlin]]) alocam blocos contíguos de memória, preservando índices fixos e custo constante para leitura escrita, enquanto exigem cópias integrais para redimensionamento. Listas mutáveis como `ArrayList<T>` em Java ou `MutableList<T>` em Kotlin encapsulam um array interno expansível, duplicando a capacidade quando o limite é atingido e mantendo referências consecutivas na heap; `LinkedList<T>` em Java utiliza nós encadeados distribuídos, cada qual armazenado como objeto separado com ponteiros duplos.

Coleções sem duplicidade, como `HashSet<T>` e `MutableSet<T>`, guardam elementos em tabelas de dispersão, distribuindo referências em buckets calculados a partir do método `hashCode`, com controle de carga para equilibrar colisões. Dicionários (`HashMap<K,V>` e `MutableMap<K,V>`) compartilham o mesmo princípio de hashing, preservando pares chave-valor em entradas independentes, enquanto `SparseArray` e suas variantes otimizam pares chave-inteiro com vetores ordenados e busca binária.

## Casos de Uso
Modelos de interface em `RecyclerView` dependem de listas baseadas em arrays para difundir estados de item sem custos excessivos de acesso. Persistência temporária de identificadores ou configurações costuma utilizar `HashMap` e `SparseArray` para conciliar rapidez de busca e consumo moderado de memória, ao passo que buffers de baixo nível preferem arrays simples para evitar sobrecarga de objetos adicionais.
