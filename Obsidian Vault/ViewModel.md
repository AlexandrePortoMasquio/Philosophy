---
title: ViewModel
tags: [android, mvvm]
created: 2025-08-29
updated: 2025-08-29
---

## O que é
- Componente de apresentação que mantém estado de UI e coordena ações da tela, sobrevivendo a recriações.

## Responsabilidades

- Manter e expor o estado único da tela (UiState) como fluxo observável, preservado entre recriações e mudanças de configuração.
- Receber intents e eventos, validá-los e convertê-los em chamadas a casos de uso, combinando resultados e mapeando-os para o estado de UI.
- Coordenar concorrência: iniciar, cancelar e sequenciar tarefas assíncronas conforme o ciclo de vida; evitar chamadas duplicadas e aplicar debounce quando apropriado.
- Tratar erros e carregamento: representar carregamento, sucesso e falha de modo explícito; registrar e traduzir exceções em mensagens compreensíveis para a interface.
- Isolar efeitos: emitir eventos de navegação e mensagens de uso único sem expor APIs da View; não manter referências a widgets.
- Persistir/restaurar parte do estado quando pertinente (saved state), delegando armazenamento de longo prazo à camada de dados.
- Expor apenas superfícies estáveis (métodos de intent e estado), ocultando detalhes de implementação e dependências internas.

## Por que é necessário, e por que a View não lê os dados diretamente de useCases?

- [[Ciclo de Vida (Programação)]] e estado: o ViewModel preserva estado entre recriações e recomposições; a View, ao chamar [[UseCase|use cases]] diretamente, perderia estado, repetiria trabalho e ficaria responsável por sincronizar carregamentos/erros.
- Separação de responsabilidades: o ViewModel orquestra [[Intent (Programação)|intents]], compõe resultados de use cases, trata concorrência (cancelamento, debounce) e expõe um estado único de tela; a View apenas observa e renderiza.
- Testabilidade: sem referências a UI, a ViewModel é testável por unidade; mover chamadas de use case para a View acopla lógica a widgets e dificulta testes e evolução.
- Consistência: centralizar a leitura em uma fonte única (estado imutável) evita múltiplas origens de verdade, race conditions e efeitos colaterais espalhados pela camada de apresentação.

## Como o ViewModel controla intents?



## Diferenças (Controller vs Presenter)
- Controller (MVC): recebe input e coordena View/Model; em apps móveis costuma acumular responsabilidades e referências à View.
- Presenter (MVP): empurra atualizações para a View via interface; exige boilerplate de contrato e ainda segura referência à View.
- ViewModel (MVVM): expõe estado reativo (StateFlow/LiveData) e a View observa; não referencia a View, é lifecycle‑aware e mais testável.

## Boas práticas
- Expor `StateFlow<UiState>` e intents; nenhuma referência a APIs de View/Activity.
- Delegar regras a use cases; injetar dependências por construtor (DI).

## Ligações
- [[Arquitetura MVVM]] · [[Arquitetura Android]] · [[KMP]]
