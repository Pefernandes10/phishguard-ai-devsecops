"""Classificador de demonstração treinado com e-mails integralmente sintéticos.

ATENÇÃO: modelo ilustrativo. Não usar como bloqueador autônomo de e-mails reais.
"""
from functools import lru_cache
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

PHISHING_EXAMPLES = [
    "URGENTE: sua conta foi bloqueada, clique no link e confirme a senha",
    "Seu banco pede atualização de cadastro, informe CPF e senha agora",
    "Detectamos atividade incomum, valide o token neste endereço externo",
    "Você ganhou um prêmio! resgate imediatamente pagando uma pequena taxa",
    "Sua fatura está vencida, pague hoje neste link para evitar suspensão",
    "Atualização de segurança obrigatória, digite sua senha no formulário",
    "RH: revise seus dados bancários no portal enviado abaixo com urgência",
    "Oferta imperdível, confirme cartão e código de segurança para receber",
    "O acesso ao seu email foi suspenso, restaure sua conta nesta página",
    "Recebimento de encomenda parado, pague taxa pelo link a seguir",
    "Seu PIX foi cancelado, informe credenciais para recuperar o valor",
    "Último aviso: sua conta expira hoje, entre com usuário e senha",
    "Inconsistência fiscal identificada, abra o anexo e habilite macros",
    "Sua assinatura será cortada, atualize pagamento em nosso site alternativo",
    "Parabéns você ganhou uma promoção, compartilhe seus dados pessoais",
    "Alerta da empresa: clique imediatamente e informe a senha corporativa",
    "Equipe de TI solicita envio de código MFA para validar seu dispositivo",
    "Aviso de bloqueio imediato: libere acesso enviando CPF e senha",
    "Falso suporte técnico pede instalação de programa de acesso remoto",
    "Para evitar multa, faça transferência via PIX para chave informada",
    "Recuperação de conta pendente: clique para redefinir credenciais",
    "Seu pacote não será entregue sem informar o número do cartão",
    "Alerta urgente de atividade suspeita: confirmação de token por mensagem",
    "Central antifraude solicita sua senha e código enviado por SMS",
]

NORMAL_EXAMPLES = [
    "Reunião de equipe confirmada para terça às 10h na sala principal",
    "Segue a ata da reunião e o cronograma da próxima sprint",
    "O relatório mensal está disponível no diretório interno da equipe",
    "Podemos agendar uma conversa sobre o andamento do projeto amanhã?",
    "A apresentação acadêmica será realizada na sexta-feira às 19h",
    "Encaminho a documentação revisada para comentários até quinta-feira",
    "O professor divulgou o material de estudo no ambiente da disciplina",
    "A equipe concluiu as tarefas previstas para a semana atual",
    "Boa tarde, seguem as notas da reunião de alinhamento de ontem",
    "Favor revisar o código do pull request quando tiver disponibilidade",
    "Nosso encontro do grupo de pesquisa foi remarcado para segunda",
    "O calendário de entregas foi atualizado com os marcos do projeto",
    "Segue a lista de presença da oficina de segurança da informação",
    "A avaliação da turma acontecerá no laboratório de informática",
    "Compartilho o link público do manual técnico para consulta",
    "A biblioteca confirmou o horário de funcionamento durante a semana",
    "O time publicou a versão atualizada do documento de arquitetura",
    "Obrigado por participar da apresentação e enviar suas sugestões",
    "O trabalho de redes deve ser apresentado junto com o relatório final",
    "Gostaria de solicitar uma reunião para discutir o orçamento aprovado",
    "A monitoria de programação começa às 14 horas no campus",
    "O professor enviou o gabarito e comentou as principais dúvidas",
    "Atas e decisões estão registradas no repositório interno autorizado",
    "A equipe vai revisar amanhã os resultados dos testes unitários",
]

MODEL_VERSION = "didatico-tfidf-logreg-1.0"
INDICATOR_PATTERNS = {
    "Urgência / pressão": r"\b(urgente|imediat|último aviso|expira hoje|bloquead|suspens)\w*",
    "Pedido de credencial": r"\b(senha|token|c[oó]digo mfa|credenciais)\b",
    "Solicitação financeira": r"\b(pix|cart[aã]o|taxa|pagamento|transfer[eê]ncia)\b",
    "Link / ação externa": r"\b(clique|link|formul[aá]rio|site alternativo)\b",
}

@lru_cache(maxsize=1)
def get_model() -> Pipeline:
    training_texts = PHISHING_EXAMPLES + NORMAL_EXAMPLES
    labels = [1] * len(PHISHING_EXAMPLES) + [0] * len(NORMAL_EXAMPLES)
    model = Pipeline([
        ("tfidf", TfidfVectorizer(strip_accents="unicode", ngram_range=(1, 2), min_df=1)),
        ("clf", LogisticRegression(max_iter=1500, class_weight="balanced", random_state=42)),
    ])
    model.fit(training_texts, labels)
    return model


def analyze_text(subject: str, body: str) -> dict:
    content = f"{subject.strip()} {body.strip()}"
    probability = float(get_model().predict_proba([content])[0][1])
    risk = "alto" if probability >= 0.65 else "médio" if probability >= 0.35 else "baixo"
    indicators = [name for name, pattern in INDICATOR_PATTERNS.items()
                  if re.search(pattern, content, flags=re.IGNORECASE)]
    return {
        "risk": risk,
        "score": round(probability, 3),
        "indicators": indicators,
        "model_version": MODEL_VERSION,
        "notice": "Triagem acadêmica. Resultado probabilístico, não definitivo; valide com um analista.",
    }
