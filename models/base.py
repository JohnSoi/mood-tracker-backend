"""Модуль базовой модели"""

__author__: str = "Digital Horizons"

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

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Атрибут для задания имени таблицы исходя из названия класса

        Returns:
            str: название для таблицы в БД
        """
        return cls.__name__.lower()
