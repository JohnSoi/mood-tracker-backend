"""Модуль модели сессий пользователей"""

__author__: str = "Digital Horizons"

from datetime import datetime

from sqlalchemy import ForeignKey, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.session import MAX_IP_LENGTH, MAX_LOCATION_STR
from models.access_data import AccessData
from models.base import BaseModel
from models.mixins import TimestampMixin


class Session(BaseModel, TimestampMixin):
    """
    Модель с данными сессии

    Attributes:
        token (str): токен сессии
        ip (str): адрес доступа
        agent (str): агент пользователя
        location (str): координаты локации
        address (str): адрес, откуда произошел вход
        deactivated_at (datetime): дата отключения сессии
        access_data_id (int): идентификатор связанных данных доступа в систему
        access_data (AccessData): данные доступа в систему

    Examples:
        >>> from models import SessionModel
        >>>
        >>> session: SessionModel = SessionModel()
        >>> # Получение токена сессии
        >>> print(session.token)
    """

    token: Mapped[str] = mapped_column(Text, unique=True, index=True, nullable=False)
    ip: Mapped[str] = mapped_column(String(MAX_IP_LENGTH), nullable=True)
    agent: Mapped[str] = mapped_column(Text, nullable=True)
    location: Mapped[str] = mapped_column(String(MAX_LOCATION_STR), nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)
    deactivated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    access_data_id: Mapped[int] = mapped_column(
        ForeignKey("access_data.id", ondelete="CASCADE"), nullable=False
    )
    access_data: Mapped["AccessData"] = relationship("AccessData")

    @property
    def session_active(self) -> bool:
        """
        Признак активной сессии пользователя

        Returns:
            bool: сессия пользователя активна

        Examples:
            >>> from models import SessionModel
            >>>
            >>> session: SessionModel = SessionModel(...)
            >>> # True - если активна сессия, данные доступа в систему и сам пользователь не удален
            >>> print(session.session_active)

        Notes:
            Сессия считается активной если активная она сама, данные доступа и пользователь не удален
        """
        return all(
            (
                not self.deactivated_at,
                not self.access_data.deactivated_at,
                not self.access_data.user.deleted_at,
            )
        )
