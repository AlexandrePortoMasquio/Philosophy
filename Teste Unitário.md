# Teste Unitário
* [[MockK]]
* Testa-se as funções públicas, e as privadas são testadas indiretamente, pois são chamadas pelas públicas
* Não se testa interface, mas sim implementação, que contém a lógica.
* @RelaxedMockK para Mocks de dependências (não serão testadas)
* @InjectMockKs para o subject do teste que recebe as dependências.
* GIVEN (dependência) WHEN (evento) THEN (resultado)
* verifyExactlyOnce(o resultado esperado), verifyNever(o que deve não acontecer no resultado)