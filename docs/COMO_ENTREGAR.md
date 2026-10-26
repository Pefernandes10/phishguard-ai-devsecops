# Como entregar a atividade (+2)

## 1. Arquivos e evidências
- Apresentação com 10 slides, imagens, URLs e informações técnicas: `docs/PhishGuardAI_Apresentacao_DevSecOps.pptx`.
- Código-fonte da IA e interface: `app/`.
- Pipeline DevSecOps: `.github/workflows/security.yml`.
- Acervo de seis prompts: `prompts/`.
- Matriz de riscos e plano de implantação: `docs/`.

## 2. Executar no Windows sem mexer na política de scripts do PowerShell
Abra um PowerShell **na pasta principal** e execute:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Abra `http://127.0.0.1:8000` no navegador, clique em **Preencher exemplo** e depois em **Analisar mensagem**.

## 3. Enviar ao GitHub
1. Crie um repositório em https://github.com/new.
2. No terminal, execute:

```powershell
git init
git branch -M main
git add .
git commit -m "Projeto PhishGuard AI + DevSecOps"
git remote add origin https://github.com/SEU_USUARIO/phishguard-ai-devsecops.git
git push -u origin main
```

Se você já tiver um repositório ou Git não configurado, adapte os comandos conforme as instruções do GitHub. Não faça commit da pasta `.venv` nem de arquivos `.env`.

## 4. Registrar evidências (prints)
- Terminal exibindo `7 passed` após `pytest -q`.
- Tela principal com mensagem **fictícia** e classificação da IA.
- GitHub mostrando pasta `prompts` com 6 arquivos.
- Aba **Actions** com execução do workflow (e correções de eventuais falhas).
- Se for publicar: URL de serviço e endpoint `/health`.

## 5. Antes de enviar o slide
Atualize a última lâmina com o endereço **real** do seu GitHub. O pacote original não tem repositório público nem site hospedado. Não declare que Trivy, Bandit ou pip-audit passaram sem rodar e registrar a execução.
