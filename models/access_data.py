"""Модуль модели доступа к данным"""

__author__: str = "Digital Horizons"

import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.access_data import MAX_LOGIN_LENGTH
from models.base import BaseModel


class AccessData(BaseModel):
    login: Mapped[str] = mapped_column(String(MAX_LOGIN_LENGTH), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(Text, nullable=False)
    deactivated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), unique=True, index=True)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="access_data",
        single_parent=True
    )
