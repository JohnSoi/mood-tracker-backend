"""Модуль миксинов для моделей"""

__author__: str = "Digital Horizons"

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class TimestampMixin:
    """
    Миксин меток времени создания и обновления записи

    Attributes:
        created_at (datetime): метка времени создания записи
        updated_at (datetime): метка времени последнего изменения записи

    Examples:
        >>> from models.base import BaseModel
        >>> from models.mixins import TimestampMixin
        >>>
        >>> class User(BaseModel, TimestampMixin):
        ...     ...
        >>>
        >>> user: User = User()
        >>> # Вывод даты создания записи пользователя
        >>> print(user.created_at)

    Notes:
        При создании не нужно заполнять данные поля - они устанавливаются автоматически
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class DeletedAtMixin:
    """
    Микисин метки времени удаления записи.

    Attributes:
        deleted_at (datetime): метка времени удаления записи. Позволяет не удалять запись фактически

    Examples:
        >>> from models.base import BaseModel
        >>> from models.mixins import DeletedAtMixin
        >>>
        >>> class User(BaseModel, DeletedAtMixin):
        ...     ...
        >>>
        >>> user: User = User()
        >>> # Вывод даты удаления записи пользователя
        >>> print(user.deleted_at)

    """

    deleted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
