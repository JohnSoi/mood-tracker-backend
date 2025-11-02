"""Модуль модели связи тегов и записей настроения"""

__author__: str = "Digital Horizons"

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class MoodEntryTags(BaseModel):
    """
    Модель связи тегов с записью настроения

    Attributes:
        mood_entry_id (int): идентификатор связанной записи настроения
        tag_id (int): идентификатор связанного тега
    """
    mood_entry_id: Mapped[int] = mapped_column(
        ForeignKey("mood_entry.id", ondelete="CASCADE"), index=True, nullable=True
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tag.id", ondelete="CASCADE"), index=True, nullable=True
    )
