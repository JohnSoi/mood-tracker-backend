from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from consts.mood_entry import MoodEntryPublishStatus
from models.base import BaseModel


class MoodEntryVisibility(BaseModel):
    """
    Модель видимости записи настроения для конкретных пользователей

    Attributes:
        mood_entry_id (int): идентификатор связанной записи настроения
        user_id (int): идентификатор связанного пользователя
        status (MoodEntryPublishStatus): статус публикации записи
    """
    mood_entry_id: Mapped[int] = mapped_column(
        ForeignKey("mood_entry.id", ondelete="CASCADE"), index=True, nullable=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), index=True, nullable=False
    )
    status: Mapped[MoodEntryPublishStatus] = mapped_column(
        Enum(
            MoodEntryPublishStatus,
            name="mood_visibility_status_enum",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        index=True,
        default=MoodEntryPublishStatus.FOR_ALL_EXCLUDED_USER,
    )