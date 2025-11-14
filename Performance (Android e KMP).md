
··················
## Como usar coroutines, threads e [[Dispatcher (Android)|dispatchers]] de forma performática?

- Evite bloquear threads: nunca use chamadas bloqueantes (ex.: Thread.sleep, APIs síncronas de rede) dentro de corrotinas em dispatchers compartilhados (Main, Default, IO). Se precisar bloquear, crie um dispatcher dedicado (withContext(newSingleThreadContext(...))) ou migre para APIs suspensas reais.
  - Preserve afinidade de contexto: use Dispatchers.Main para qualquer atualização de UI e mude explicitamente com withContext(Dispatchers.IO) ou Default para trabalho pesado. Não faça compute pesado no Main nem IO no Default para não concorrer com tarefas CPU-bound.
  - Não estoure o pool: Dispatchers.IO já é elástico; não crie vários pools customizados sem
    necessidade. Reaproveite dispatchers compartilhados e ajuste limites apenas se tiver medição que
    justifique.
  - Estruture escopos corretamente: use viewModelScope, lifecycleScope, rememberCoroutineScope para
    que corrotinas cancelem junto com o lifecycle correspondente. Cancelações rápidas evitam threads
    ocupadas à toa e vazamentos de recursos.
  - Prefira APIs suspensas a callbacks: operações suspensas liberam a thread enquanto esperam I/O e
    retomam depois, aumentando throughput. Se converter callback -> suspenso, certifique-se de retomar
    no dispatcher certo (suspendCancellableCoroutine + withContext se necessário).
  - Controle concorrência explicitamente: para fan-out/fan-in use async/await, Channel,
    Semaphore etc. Evite lançar dezenas de corrotinas descontroladas; limite paralelismo com
    Dispatcher.limitedParallelism(n) ou semáforos.
  - Medir antes de otimizar: use profilers (Systrace, CPU profiler, coroutine debugger) para identificar
    gargalos reais. Ajustes em dispatchers ou número de threads só fazem sentido com dados; suposições
    podem piorar latência ou consumo.