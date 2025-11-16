"""Модуль для настроки и работы с логером"""

__author__: str = "Digital Horizons"

import sys
from logging import Logger

from loguru import logger

from logger.config import LoggerConfig
from logger.consts import JSON_FORMAT, TEXT_FORMAT


def setup_logger() -> Logger:
    """
    Создание настроенного логгера приложения

    Returns:
        Logger: настроенный экземпляр логгера

    Examples:
        >>> from logger.common import setup_logger
        >>>
        >>> app_logger: Logger = setup_logger()
    """
    config: LoggerConfig = LoggerConfig()

    # Удаляем стандартный обработчик
    logger.remove()

    # Консольный вывод (всегда)
    logger.add(
        sys.stdout,
        format=config.log_format,
        level=config.log_level,
        colorize=True,
        backtrace=True,
        diagnose=True,
    )

    # Файловый вывод для production
    if config.environment == "production":
        # Логи ошибок
        logger.add(
            config.log_path / "error.log",
            format=JSON_FORMAT,
            level="ERROR",
            rotation="10 MB",
            retention="30 days",
            compression="zip",
            backtrace=True,
            diagnose=False,  # В production не показываем детали отладки
        )

        # Все логи
        logger.add(
            config.log_path / "app.log",
            format=JSON_FORMAT,
            level="INFO",
            rotation="50 MB",
            retention="7 days",
            compression="zip",
            backtrace=False,
            diagnose=False,
        )

    # Логи для разработки
    else:
        logger.add(
            config.log_path / "debug.log",
            format=TEXT_FORMAT,
            level="DEBUG",
            rotation="10 MB",
            retention="3 days",
            compression="zip",
        )

    # Логи HTTP запросов
    logger.add(
        config.log_path / "http.log",
        format=JSON_FORMAT,
        level="INFO",
        filter=lambda record: "http" in record["extra"],
        rotation="20 MB",
        retention="14 days",
        compression="zip",
    )

    return logger


# Глобальный экземпляр логгера
app_logger: Logger = setup_logger()
