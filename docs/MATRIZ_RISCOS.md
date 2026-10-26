# Matriz de riscos — versão inicial (qualitativa e não auditada)

| ID | Risco | Impacto | Controle atual no protótipo | Lacuna antes de produção |
|---|---|---|---|---|
| R1 | Dependência Python vulnerável | Alto | pip-audit no CI; versões definidas | SBOM e política de atualização contínua |
| R2 | Imagem de contêiner com CVE | Alto | Trivy no CI; processo sem root | Imagem base imutável; pin digest |
| R3 | Texto pessoal vazado em logs | Alto | Sem armazenamento de mensagens no app; sem access log no Docker | Revisar logs no proxy, servidor e provedor |
| R4 | Abuse de API / DoS | Alto | Limite de tamanho de entrada | Autenticação e rate limiting por gateway |
| R5 | Erro/falso negativo do modelo | Alto | Aviso de incerteza, revisão humana | Dataset representativo, métricas e monitoramento de drift |
| R6 | Manipulação / envenenamento de treino | Alto | Dataset sintético versionado no código | Assinatura/proveniência e revisão de dados |
| R7 | Inserção de HTML / XSS | Médio | Resposta JSON; `textContent`; CSP; testes | Pentest do ambiente publicado |
| R8 | Fluxo CI comprometido | Alto | Token `contents: read` | Pin SHA das Actions; regras de branches/review |

**Importante:** riscos e controles foram mapeados; não equivalem a laudo de pentest ou certificação de conformidade.
