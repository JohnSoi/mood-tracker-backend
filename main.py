from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from core.config import settings
from logger import logging_middleware
from security import setup_cors

app: FastAPI = FastAPI(
    title=settings.APP_NAME,
    description="БЛ приложения для отслеживания настроения",
    docs_url="/docs" if settings.environment != "production" else None
)

setup_cors(app)


@app.middleware("http")
async def add_logging_middleware(request: Request, call_next):
    return await logging_middleware(request, call_next)


@app.get("/")
def read_root():
    """Редирект на страницу документации"""
    return RedirectResponse(url="/docs")
