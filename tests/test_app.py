"""Testes de contrato e validação de entradas para demonstração acadêmica."""
from fastapi.testclient import TestClient
from app.main import app
from app.model import analyze_text

client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'ok'


def test_analyze_returns_proba_and_notice():
    response = client.post('/analyze', json={
        'subject': 'Aviso sobre conta',
        'body': 'Clique neste link e informe a sua senha para validar a conta imediatamente.',
    })
    assert response.status_code == 200
    data = response.json()
    assert 0 <= data['score'] <= 1
    assert data['risk'] in {'alto', 'médio', 'baixo'}
    assert data['indicators']
    assert 'não definitivo' in data['notice']


def test_short_input_blocked():
    response = client.post('/analyze', json={'subject': 'a', 'body': 'x'})
    assert response.status_code == 422


def test_oversized_body_blocked():
    response = client.post('/analyze', json={'subject': 'Teste', 'body': 'A' * 5100})
    assert response.status_code == 422


def test_xss_payload_not_reflected():
    payload = '<script>alert(1)</script>'
    response = client.post('/analyze', json={'subject': 'Teste', 'body': payload})
    assert response.status_code == 200
    assert payload not in response.text


def test_security_headers():
    response = client.get('/')
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert response.headers['X-Frame-Options'] == 'DENY'
    assert "object-src 'none'" in response.headers['Content-Security-Policy']
    assert response.headers['Cache-Control'] == 'no-store'


def test_model_deterministic():
    a = analyze_text('Atualização', 'Clique no link e informe sua senha agora.')
    b = analyze_text('Atualização', 'Clique no link e informe sua senha agora.')
    assert a == b
