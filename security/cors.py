"""Модуль для настройки CORS"""

__author__: str = "Digital Horizons"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings, get_cors_origins
from logger import app_logger


def setup_cors(app: FastAPI) -> None:
    """
    Устанавливает настройки CORS на экзепляре приложения

    Args:
        app (FastAPI): экземплар приложения FastAPI

    Examples:
        >>> from fastapi import FastAPI
        >>> from security import setup_cors
        >>>
        >>> app: FastAPI = FastAPI()
        >>> setup_cors(app)
    """
    origins: list[str] = get_cors_origins(settings.DEBUG)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=[
            "Content-Type",
            "Authorization",
            "X-Requested-With",
            "Accept",
            "Origin",
            "X-CSRF-Token",
        ],
        expose_headers=[
            "Content-Range",
            "X-Total-Count",
        ],
        max_age=600,
    )

    # Логирование для отладки
    app_logger.info(f"CORS configured for environment: {settings.environment}")
    app_logger.info(f"Allowed origins: {origins}")