"""Модуль модели отношений пользователей"""

__author__: str = "Digital Horizons"

from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from consts.friendship import FriendshipStatus
from models.base import BaseModel
from models.mixins import TimestampMixin


class FriendShip(BaseModel, TimestampMixin):
    """
    Модель отношений пользователей - друзья

    Attributes:
        sender_request_user_id (int): идентификатор пользователя отправителя запроса в друзья
        recipient_request_user_id (int): идентификатор пользователя получателя запроса в друзья
        status (FriendshipStatus): статус запроса в друзья

    Examples:
        >>> # Статус в ожидании принятия
        >>> friendship_status = FriendshipStatusModel()
        >>> # Статус принятия запроса в друзья
        >>> friendship_status_accept = FriendshipStatusModel(status=FriendshipStatus.ACCEPTED)
    """
    sender_request_user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), unique=True, index=True
    )
    recipient_request_user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), unique=True, index=True
    )
    status: Mapped[FriendshipStatus] = mapped_column(
        Enum(
            FriendshipStatus,
            name="friend_ship_status_enum",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        index=True,
        default=FriendshipStatus.PENDING
    )
