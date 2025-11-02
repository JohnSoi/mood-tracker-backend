"""Модуль базовой модели"""

__author__: str = "Digital Horizons"

import re

from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy import Integer


class BaseModel(DeclarativeBase):
    """
    Базовая модель.

    Examples:
        >>> from models.base import BaseModel
        >>>
        >>> # Модель пользователя с названием для таблиц "user"
        >>> class User(BaseModel):
        ...     ...

    Notes:
        Используется только для наследования другими моделями с реализацией
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Атрибут для задания имени таблицы исходя из названия класса

        Returns:
            str: название для таблицы в БД
        """
        # Обрабатываем последовательности заглавных букв (аббревиатуры)
        name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", cls.__name__)
        # Вставляем подчеркивание перед заглавными, которые идут после строчных
        name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
        # Конвертируем в нижний регистр
        return name.lower()
