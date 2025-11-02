"""Модуль модели записи настроения"""

__author__: str = "Digital Horizons"

from sqlalchemy import SmallInteger, Text, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.mood_entry import MoodEntryPublishStatus
from .base import BaseModel
from .mixins import TimestampMixin, DeletedAtMixin
from .tags import Tag
from .user import User


class MoodEntry(BaseModel, TimestampMixin, DeletedAtMixin):
    """
    Модель для записи настроения

    Attributes:
        score (int): оценка состояния настроения
        description (str): описание своих впечатлений и мыслей
        status (MoodEntryPublishStatus): статус публикации записи
        user_id (int): идентификатор связанного пользователя
        user (UserModel): данные о связанном пользователе
    """
    score: Mapped[int] = mapped_column(SmallInteger, default=0, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[MoodEntryPublishStatus] = mapped_column(
        Enum(
            MoodEntryPublishStatus,
            name="mood_publish_status_enum",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        index=True,
        default=MoodEntryPublishStatus.FOR_ALL,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), index=True, nullable=True
    )

    user: Mapped["User"] = relationship("User")
    tags: Mapped[list[Tag]] = relationship("Tag")

