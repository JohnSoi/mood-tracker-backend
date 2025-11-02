"""Модуль модели тегов"""

__author__: str = "Digital Horizons"

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.tag import MAX_TAG_NAME_LENGTH, MAX_COLOR_LENGTH
from models.base import BaseModel
from models.user import User


class Tag(BaseModel):
    """
    Модель для работы с тегами

    Attributes:
        name (str): название тега
        color (str): цвет оформления тега
        user_id (int | None): идентификатор связанного пользователя. Параметры без него считаются общими
        user (UserModel | None): данные о связанном пользователе

    Examples:
        >>> # Создание тега для работы
        >>> tag = Tag(name="Работа", color="red", user_id=1)
    """
    name: Mapped[str] = mapped_column(String(MAX_TAG_NAME_LENGTH), unique=True, nullable=False)
    color: Mapped[str] = mapped_column(String(MAX_COLOR_LENGTH))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), index=True, nullable=True
    )

    user: Mapped["User"] = relationship("User")
