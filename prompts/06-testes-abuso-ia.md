# Prompt 06 — Testes de abuso e robustez
**Objetivo:** testar segurança e confiabilidade da aplicação.

> Defina uma bateria de testes benignos e autorizados para o classificador de phishing, usando somente e-mails fictícios. Cubra mensagens longas, entradas vazias, HTML, conteúdo enganoso, erros de classificação, manipulação por palavras-chave e ausência de dados pessoais nos logs. Informe esperado × observado e como registrar evidências. Não afirme que um teste passou sem executá-lo.

**Entrada:** contrato da API e limites de entrada.
**Saída esperada:** matriz de testes para pytest e avaliação do modelo.
**Validação humana:** rodar os testes, guardar logs e resultados.
