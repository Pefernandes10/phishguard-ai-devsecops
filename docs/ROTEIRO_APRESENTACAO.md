# Roteiro rápido para apresentar — PhishGuard AI

**Slide 1 — Abertura**
> Meu projeto se chama PhishGuard AI. É uma prova de conceito que utiliza inteligência artificial para analisar mensagens suspeitas. A ideia é demonstrar a implantação e como incluir segurança no desenvolvimento, utilizando DevSecOps.

**Slide 2 — Problema**
> Golpes de phishing costumam explorar urgência e pedidos de senha. O programa recebe um texto de exemplo, analisa o conteúdo e indica se há sinais suspeitos. A decisão final continua sendo humana.

**Slide 3 — Arquitetura**
> A pessoa preenche o formulário web, o FastAPI valida os campos, e o modelo de inteligência artificial processa o texto. O resultado volta em JSON. O protótipo usa dados fictícios e não tem banco de dados.

**Slide 4 — Funcionamento da IA**
> Utilizei TF-IDF, que transforma texto em números, e regressão logística, que aprende padrões. O treino contém 48 mensagens fictícias. O exemplo demonstrado resultou em cerca de 68% de score de phishing; esse número não é uma medida de precisão em produção.

**Slide 5 — DevSecOps**
> O GitHub Actions contém testes com Pytest, análise estática com Bandit, auditoria de bibliotecas com pip-audit e verificação de imagem Docker com Trivy. Caso encontre problemas bloqueantes, o pipeline não deve permitir um deploy automático.

**Slide 6 — Vulnerabilidades**
> Levantei riscos de dependências vulneráveis, sobrecarga de API, execução de scripts em interface e falsos diagnósticos. Alguns controles já estão no código, enquanto autenticação e limitação de requisições ainda precisam ser acrescentados antes de um uso real.

**Slide 7 — Conformidade**
> A aplicação foi planejada respeitando princípios como finalidade e necessidade da LGPD. A governança usa ideias do NIST AI Risk Management Framework. Como é um protótipo, isso não equivale a certificação ou conformidade jurídica garantida.

**Slide 8 — Prompts no GitHub**
> Montei seis prompts em arquivos Markdown, cobrindo arquitetura segura, modelagem de ameaças, code review, LGPD, incidentes e testes de abuso. Eles ficam versionados no GitHub. São prompts de apoio ao desenvolvimento, e não o modelo usado na classificação.

**Slide 9 — Implantação**
> O protótipo roda localmente com FastAPI ou Docker. Após publicar no GitHub, o CI executa as verificações. O arquivo render.yaml define como seria implantado no Render, condicionando a publicação à aprovação dos checks.

**Slide 10 — Entrega**
> Como evidência, tenho o código, os testes locais, a documentação, o acervo de prompts e a apresentação. Depois de publicar no GitHub, devo anexar também a execução do Actions e o link do repositório, além de uma URL real se for implantado.
