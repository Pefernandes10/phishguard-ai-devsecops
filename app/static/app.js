const form = document.getElementById('form');
const submitButton = document.getElementById('submit');
document.getElementById('demo').addEventListener('click', () => {
  document.getElementById('subject').value = 'URGENTE: bloqueio de conta';
  document.getElementById('body').value = 'Sua conta foi bloqueada. Clique no link e informe sua senha e token MFA imediatamente para liberar o acesso.';
});
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  submitButton.disabled = true;
  submitButton.textContent = 'Analisando...';
  try {
    const res = await fetch('/analyze', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({subject: document.getElementById('subject').value,
                            body: document.getElementById('body').value}),
    });
    if (!res.ok) throw new Error('Falha na validação ou no servidor');
    const data = await res.json();
    const risk = document.getElementById('risk');
    risk.textContent = data.risk.toUpperCase();
    risk.className = 'risk ' + (data.risk === 'alto' ? 'high' : (data.risk === 'médio' ? 'medium' : 'low'));
    document.getElementById('score').textContent = Math.round(data.score * 100) + '%';
    document.getElementById('fill').style.width = Math.round(data.score * 100) + '%';
    const list = document.getElementById('hints');
    list.replaceChildren();
    const items = data.indicators.length ? data.indicators : ['Nenhum indicador textual da lista foi encontrado'];
    items.forEach((item) => {const li = document.createElement('li'); li.textContent = item; list.appendChild(li);});
    document.getElementById('disclaimer').textContent = data.notice;
  } catch (err) {
    document.getElementById('risk').textContent = 'Erro na análise';
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = 'Analisar mensagem →';
  }
});
