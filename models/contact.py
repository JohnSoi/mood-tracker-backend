"""Модуль для модели контактных данных"""

__author__: str = "Digital Horizons"

import datetime

from sqlalchemy import DateTime, String, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.contact import ContactType, CONTACT_VALUE_LENGTH
from .base import BaseModel
from .mixins import TimestampMixin, DeletedAtMixin
from .user import User


class Contact(BaseModel, TimestampMixin, DeletedAtMixin):
    """
    Модель контактных данных

    Attributes:
        value (str): значение контакта
        type (ContactType): тип контакта
        other_type (str | None): тип контакта, если он ен из спсика доступных
        verified_at (datetime | None): дата подтверждения контакта
        deactivated_at (datetime | None): дата дективации контакта
        user_id (int): идентификатор связанного пользователя
        user (UserModel): модель с данными о пользователе

    Examples:
        >>> from models import ContactModel
        >>> from consts.contact import ContactType
        >>>
        >>> # создание контакта мобильного телефона
        >>> contact: ContactModel = ContactModel(value="89999999999", type=ContactType.PHONE)
        >>> # Создание контакта другого типа
        >>> contact_other: ContactModel = ContactModel(value="89999999999", type=ContactType.OTHER, other_type="Skype")
    """

    value: Mapped[str] = mapped_column(
        String(CONTACT_VALUE_LENGTH), nullable=False, unique=True, index=True
    )
    type: Mapped[ContactType] = mapped_column(
        Enum(
            ContactType,
            name="contact_type_enum",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        index=True,
    )
    other_type: Mapped[str] = mapped_column(String(CONTACT_VALUE_LENGTH), nullable=True)
    verified_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    deactivated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), unique=True, index=True
    )

    user: Mapped["User"] = relationship("User")
