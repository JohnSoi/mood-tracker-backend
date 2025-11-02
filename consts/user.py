"""Константы для работы с пользователем"""

__author__: str = "Digital Horizons"

from enum import StrEnum

# Максимальная длинна для полей ФИО
NAME_LENGTH: int = 50


class UserGender(StrEnum):
    """
    Пол пользователя системы

    Attributes:
        MALE (str): мужской
        FEMALE (str): женский

    Examples:
        >>> from sqlalchemy import String, Enum
        >>> from sqlalchemy.orm import Mapped, mapped_column
        >>>
        >>> from consts.user import UserGender
        >>> from models.base import BaseModel
        >>> from models.mixins import TimestampMixin, DeletedAtMixin
        >>>
        >>>
        >>> # Использование перечисления как тип поля модели
        >>> class User(BaseModel, TimestampMixin, DeletedAtMixin):
        ...     gender: Mapped[UserGender] = mapped_column(
        ...         Enum(
        ...             UserGender,
        ...             name="user_gender_enum",
        ...             values_callable=lambda x: [e.value for e in x],
        ...         ),
        ...         nullable=False,
        ...         index=True,
        ...     )
        >>>
        >>> # Создание пользователя мужского рода
        >>> user: User = User(gender=UserGender.MALE)
    """

    MALE = "male"
    FEMALE = "female"
