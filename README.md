# PhishGuard AI — IA + DevSecOps

**Prova de conceito acadêmica**: aplicação web que classifica, de forma probabilística, e-mails **fictícios** quanto ao risco de phishing. Utiliza aprendizado de máquina local (TF-IDF + regressão logística), FastAPI, Docker e pipeline de testes de segurança no GitHub Actions.

> ATENÇÃO: este é um protótipo educacional. O dataset é pequeno e inteiramente sintético. O projeto não está validado para bloquear e-mails reais e **não deve receber dados pessoais**. Não há garantia de conformidade legal, nem de ausência de vulnerabilidades.

## Objetivos do trabalho
- Criar e implantar uma aplicação com IA.
- Integrar testes e scanners à rotina DevSecOps.
- Mapear riscos, vulnerabilidades e controles de privacidade.
- Manter um **acervo versionado de seis prompts** na pasta [`prompts/`](prompts/).
- Disponibilizar a arquitetura, plano de implantação e apresentação.

## Executar em ambiente virtual

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Abra: `http://127.0.0.1:8000` | Swagger: `http://127.0.0.1:8000/docs`.

## Testes e scanners

```bash
python -m pip install -r requirements-dev.txt
pytest -q
bandit -r app -ll
pip-audit -r requirements.txt
```

**Docker:**
```bash
docker build -t phishguard-ai .
docker run --rm -p 8000:8000 phishguard-ai
```

## Exemplo da API

```bash
curl -X POST http://127.0.0.1:8000/analyze \
  -H 'Content-Type: application/json' \
  -d '{"subject":"Aviso urgente","body":"Clique no link e informe sua senha e token imediatamente."}'
```

O retorno tem nível de risco, probabilidade, sinais textuais e alerta de incerteza. A **probabilidade não foi calibrada em dados reais** e não deve ser interpretada como confiabilidade comprovada.

## Segurança já implementada vs. em planejamento

**Implementado no código:** validação de tamanho, dataset fictício, ausência de persistência de mensagens, resultado em JSON, renderização textual no navegador, cabeçalhos HTTP defensivos, usuário não privilegiado no Docker, testes de contrato e scanners no workflow (sujeitos a execução no GitHub).

**A implantar para produção:** autenticação, autorização, limites de taxa por gateway, monitoramento, revisão do provedor de logs, métricas externas de qualidade do modelo, proteção de branch e versões imutáveis/digests de Actions e imagens, avaliação legal e de privacidade.

## Arquivos

```text
app/                    API, IA e interface web
.github/workflows/       CI com pytest, Bandit, pip-audit, Trivy
prompts/                 Acervo de seis prompts + modo de uso
tests/                   Testes unitários/API
docs/                    Matriz de riscos e plano de implantação
Dockerfile               Imagem executada por usuário sem root
render.yaml              Blueprint para publicar no Render
```


## Fontes oficiais
- LGPD: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP Top 10 (Web): https://owasp.org/www-project-top-ten/
- OWASP Top 10 para LLM/GenAI 2026: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- GitHub Actions Security: https://docs.github.com/en/actions/how-tos/secure-your-work
- Trivy Action: https://github.com/aquasecurity/trivy-action
- pip-audit: https://github.com/pypa/pip-audit
- Render Blueprints: https://render.com/docs/blueprint-spec
