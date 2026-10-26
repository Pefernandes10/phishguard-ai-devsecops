# Prompt 03 — Revisão segura de código
**Objetivo:** ampliar a análise humana e do SAST.

> Revise o trecho Python/FastAPI **sem segredos e sem dados reais** para identificar validação insuficiente, exposição em logs, execução insegura, dependências, falhas de autenticação e manipulação de saída. Para cada suspeita, informe arquivo/linha, cenário realista, severidade justificada, correção sugerida e teste de regressão. Separe achado comprovado de hipótese. Não execute comandos nem exfiltre dados.

**Entrada:** arquivos de código limpos de credenciais.
**Saída esperada:** checklist de revisão de pull request.
**Validação humana:** reproduzir e corrigir antes de aceitar.
