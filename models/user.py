"""Модуль модели пользователей"""

__author__: str = "Digital Horizons"

from datetime import datetime

from sqlalchemy import String, Enum, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.user import UserGender, NAME_LENGTH
from .base import BaseModel
from .mixins import TimestampMixin, DeletedAtMixin


class User(BaseModel, TimestampMixin, DeletedAtMixin):
    """
    Модель пользователя системы

    Attributes:
        surname (str): фамилия пользователя
        name (str): имя пользователя
        patronymic (str): отчество пользователя
        gender (UserGender): пол пользователя
        remove_publish_at (datetime): время снятия с публикации отображения ФИО
        avatar_url (str): путь к аватару пользователя

    Examples:
        >>> from models.user import User
        >>>
        >>> user: User = User(...)
        >>> # Путь до аватара пользователя
        >>> print(user.avatar_url)
    """

    surname: Mapped[str] = mapped_column(
        String(NAME_LENGTH), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(NAME_LENGTH), nullable=False, index=True)
    patronymic: Mapped[str] = mapped_column(
        String(NAME_LENGTH), nullable=True, index=True
    )
    gender: Mapped[UserGender] = mapped_column(
        Enum(
            UserGender,
            name="user_gender_enum",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        index=True,
    )
    remove_publish_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    avatar_url: Mapped[str] = mapped_column(Text, nullable=True)

    access_data: Mapped["AccessData"] = relationship(
        "AccessData",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
        lazy="selectin"  # Загружаем сразу с пользователем
    )

    @property
    def full_name(self) -> str:
        """
        Полное имя пользователя

        Returns:
            str: полное имя пользователя. Отчество добавляется по наличию

        Examples:
            >>> from models.user import User
            >>>
            >>> user: User = User(name="John", surname="Doe")
            >>> # Doe John
            >>> print(user.full_name)
        """
        full_name_str: str = f"{self.surname} {self.name}"

        if self.patronymic:
            full_name_str += f" {self.patronymic}"

        return full_name_str

    @property
    def short_full_name(self) -> str:
        """
        Короткая запись полного имени

        Returns:
            str: короткая запись полного имени. Сокращает имя и отчество до 1 буквы и оканчивает из "."

        Examples:
            >>> from models.user import User
            >>>
            >>> user: User = User(name="John", surname="Doe")
            >>> # Doe J.
            >>> print(user.short_full_name)
            >>> user: User = User(name="John", surname="Doe", patronymic="Raf")
            >>> # Doe J.R.
            >>> print(user.short_full_name)
        """
        full_name_str: str = f"{self.surname} {self.name[0]}."

        if self.patronymic:
            full_name_str += f"{self.patronymic[0]}."

        return full_name_str
