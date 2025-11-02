"""Константы для работы со связями пользователей - друзьями"""

__author__: str = "Digital Horizons"

from enum import StrEnum


class FriendshipStatus(StrEnum):
    """
    Статусы взаимоотношений пользователей - друзей

    Attributes:
        PENDING (str): ожидает подтверждения
        ACCEPTED (str): запрос в друзья принят
        REJECTED (str): запрос отклонен

    Examples:
        >>> from models import FriendshipStatusModel
        >>> from sqlalchemy import Enum
        >>> from sqlalchemy.orm import Mapped, mapped_column
        >>>
        >>> from models.base import BaseModel
        >>> from models.mixins import TimestampMixin
        >>>
        >>>
        >>> # Использование в модели для статусов
        >>> class FriendShip(BaseModel, TimestampMixin):
        ...    status: Mapped[FriendshipStatus] = mapped_column(
        ...        Enum(
        ...            FriendshipStatus,
        ...            name="friend_ship_status_enum",
        ...            values_callable=lambda x: [e.value for e in x],
        ...        ),
        ...        nullable=False,
        ...        index=True,
        ...        default=FriendshipStatus.PENDING
        ...    )
        >>>
        >>> # Статус в ожидании принятия
        >>> friendship_status = FriendshipStatusModel()
        >>> # Статус принятия запроса в друзья
        >>> friendship_status_accept = FriendshipStatusModel(status=FriendshipStatus.ACCEPTED)
    """

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
