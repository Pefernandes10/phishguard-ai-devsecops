# Plano de implantação

## Regras de entrada (PR -> branch main)
- Pull request com revisão de colega.
- Suite pytest verde.
- Bandit sem achados de gravidade média/alta.
- pip-audit sem vulnerabilidade de dependência bloqueante.
- Build Docker concluído e Trivy sem HIGH/CRITICAL corrigíveis.
- Revisão de dados usados no projeto (somente sintéticos).

## Etapas de implantação
1. Executar localmente: `docker build -t phishguard-ai .`.
2. Iniciar o contêiner: `docker run --rm -p 8000:8000 phishguard-ai`.
3. Confirmar `GET http://localhost:8000/health` e enviar e-mail fictício em `/`.
4. Publicar os arquivos em repositório GitHub próprio com branch protection.
5. Conectar esse repositório ao Render por meio de **New > Blueprint** e `render.yaml`.
6. Confirmar que `autoDeployTrigger: checksPass` aguarda checks do GitHub.
7. Testar o serviço, TLS e a configuração de logs na hospedagem; monitorar novas CVEs.

## Condições para uso real
- Autenticação, autorização, rate limit, monitoramento e plano de incidentes.
- Avaliação de base legal LGPD, retenção e acordo com operadores (se cabível).
- Métricas com dataset representativo e revisão humana dos alertas.
- Fixação de imagem por digest, action SHAs e threat modeling atualizado.

**Status:** projeto e protótipo local, não há implantação pública realizada ou repositório GitHub criado automaticamente.
