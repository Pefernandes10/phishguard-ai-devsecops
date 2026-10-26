"""API da prova de conceito PhishGuard AI (sem retenção persistente de mensagens)."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.model import MODEL_VERSION, analyze_text

BASE_DIR = Path(__file__).parent
app = FastAPI(
    title="PhishGuard AI — projeto acadêmico DevSecOps",
    description="Demonstração com mensagens fictícias. Não recomendado para produção sem controles adicionais.",
    version="1.0.0",
)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


class EmailInput(BaseModel):
    subject: str = Field(min_length=3, max_length=180)
    body: str = Field(min_length=5, max_length=5000)


@app.middleware("http")
async def security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Cache-Control"] = "no-store"
    if request.url.path == "/":
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; object-src 'none'; base-uri 'none'; "
            "frame-ancestors 'none'; form-action 'self'"
        )
    return response


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}


@app.post("/analyze")
def analyze(payload: EmailInput):
    return analyze_text(payload.subject, payload.body)
