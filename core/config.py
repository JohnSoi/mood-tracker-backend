"""Модуль конфигурации приложения"""

__author__: str = "Digital Horizons"

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек приложения

    Attributes:
        APP_NAME (str): название приложения
        DEBUG (bool): режим отладки приложения
        DB_URL (PostgresDsn): адрес для подключения к БД
        SECRET_KEY (str): секретный ключ приложения для генерации защищенных данных

    Examples:
        >>> from core.config import settings
        >>> print(settings.APP_NAME)
        "mood-tracker"
    """

    APP_NAME: str = "mood-tracker"
    DEBUG: bool = False
    DB_URL: PostgresDsn
    SECRET_KEY: str

    class Config:
        """Конфиг для файла настроек"""

        env_file = ".env"


# Глобальный экземпляр настроек
settings: Settings = Settings()
