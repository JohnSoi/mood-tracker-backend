"""Модуль конфигурации приложения"""

__author__: str = "Digital Horizons"

from typing import Literal

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек приложения

    Attributes:
        APP_NAME (str): название приложения
        DEBUG (bool): режим отладки приложения
        LOG_LEVEL (str): порог логирования сообщений
        LOG_FILE_FORMAT (str): формат логов
        DB_URL (PostgresDsn): адрес для подключения к БД
        SECRET_KEY (str): секретный ключ приложения для генерации защищенных данных

    Examples:
        >>> from core.config import settings
        >>> print(settings.APP_NAME)
        "mood-tracker"
    """

    APP_NAME: str = "mood-tracker"

    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    LOG_FILE_FORMAT: Literal["json", "text"] = "json"

    DB_URL: PostgresDsn
    SECRET_KEY: str

    @property
    def environment(self) -> str:
        """
        Определяет среду работы сервиса

        Returns:
            str: "production" для боевой среды и "development" для разработки

        Examples:
            >>> from core.config import settings
            >>> print(settings.environment) # development
        """
        return "development" if self.DEBUG else "production"

    class Config:
        """Конфиг для файла настроек"""

        env_file = ".env"


def get_cors_origins(debug_mode: bool) -> list[str]:
    """
    Получение настроек разрешенных доменов в зависимости от режима работы сервиса

    Args:
        debug_mode (bool): режим отладки

    Returns:
        list[str]: список разрешенных доменов

    Examples:
        >>> from fastapi import FastAPI
        >>> from fastapi.middleware.cors import CORSMiddleware
        >>> from core.config import get_cors_origins
        >>>
        >>> app: FastAPI = FastAPI()
        >>> origins: list[str] = get_cors_origins(settings.DEBUG)
        >>>
        >>> app.add_middleware(
        >>>     CORSMiddleware,
        >>>     allow_origins=origins
        >>> )
    """
    if debug_mode:
        return [
            "http://localhost:3000",
            "http://localhost:8080",
            "http://127.0.0.1:3000",
            "http://127.0.0.1:8080",
            "http://0.0.0.0:3000",
            "http://0.0.0.0:8080",
        ]
    else:
        return []


# Глобальный экземпляр настроек
settings: Settings = Settings()
