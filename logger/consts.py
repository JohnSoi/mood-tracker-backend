"""Модуль констант логгера"""

__author__: str = "Digital Horizons"

from core.config import settings

# Формат для JSON логов
JSON_FORMAT: str = (
        "{"
        "'time': '{time:YYYY-MM-DD HH:mm:ss.SSS}', "
        "'level': '{level}', "
        "'message': '{message}', "
        "'module': '{name}', "
        "'function': '{function}', "
        "'line': '{line}', "
        "'environment': '" + settings.environment + "'"
        "}"
)

# Формат для текстовых логов (разработка)
TEXT_FORMAT: str = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)
