"""Модуль для настройки работы логера"""

__author__: str = "Digital Horizons"

from pathlib import Path

from core.config import settings
from logger.consts import JSON_FORMAT, TEXT_FORMAT


class LoggerConfig:
    """
    Класс с настрйоками поведения логера приложения

    Attributes:
        environment (str): текущая среда работы севрсиа
        log_level (str): устанавливаемы уровень логирования
        log_file_format (str): формат файла логирования

    Examples:
        >>> import sys
        >>> from loguru import logger, Logger
        >>> from logger.config import LoggerConfig
        >>>
        >>>
        >>> def setup_logger() -> Logger:
        >>>     config: LoggerConfig = LoggerConfig()
        >>>     logger.remove()
        >>>     # Консольный вывод (всегда)
        >>>     logger.add(
        >>>         sys.stdout,
        >>>         level=config.log_level,
        >>>         colorize=True,
        >>>         backtrace=True,
        >>>         diagnose=True,
        >>>     )
        >>>     return logger
    """
    def __init__(self):
        self.environment: str = settings.environment
        self.log_level: str = settings.LOG_LEVEL
        self.log_file_format: str = settings.LOG_FILE_FORMAT

    @property
    def log_path(self) -> Path:
        """
        Путь до папки хранения логов. Создает ее, если она еще не сущестсвует

        Returns:
            Path: путь до папки логов в виде инстанса Path

        Examples:
            >>> from loguru import logger
            >>>
            >>> config: LoggerConfig = LoggerConfig()
            >>> logger.add(config.log_path / "error.log")
        """
        path = Path("logs")
        path.mkdir(exist_ok=True)
        return path

    @property
    def log_format(self) -> str:
        """
        Формат тескта логов в зависимости от выбраного типа файлов

        Returns:
            str: формат записи логов

        Examples:
            Examples:
            >>> from loguru import logger
            >>>
            >>> config: LoggerConfig = LoggerConfig()
            >>> logger.add(
            >>>     config.log_path / "error.log",
            >>>     format=config.log_format,
            >>>     level=config.log_level
            >>> )
        """
        return JSON_FORMAT if self.log_file_format == "json" else TEXT_FORMAT
