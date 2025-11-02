"""Константы для работы с контактными данными"""

__author__: str = "Digital Horizons"

from enum import StrEnum

# Максимальная длинна значения контакта
CONTACT_VALUE_LENGTH: int = 50


class ContactType(StrEnum):
    """
    Тип контактных данных. Определяет будущее форматирование записи

    Attributes:
        EMAIL (str): электронная почта
        PHONE (str): мобильный телефон
        VK (str): ВК
        SITE (str): сайт
        TELEGRAM (str): телеграм
        WHATSAPP (str): WhatsApp
        VIBER (str): Viber
        OTHER (str): прочие (указывается тип в таблице contact)

    Examples:
        >>> from sqlalchemy import DateTime, String, ForeignKey, Enum
        >>> from sqlalchemy.orm import Mapped, mapped_column, relationship
        >>>
        >>> from models.base import BaseModel
        >>> from models.mixins import TimestampMixin, DeletedAtMixin
        >>>
        >>>
        >>> # Использование как тип в модели
        >>> class Contact(BaseModel, TimestampMixin, DeletedAtMixin):
        ...     value: Mapped[str] = mapped_column(String(CONTACT_VALUE_LENGTH), nullable=False, unique=True, index=True)
        ...     type: Mapped[ContactType] = mapped_column(
        ...         Enum(
        ...             ContactType,
        ...             name="contact_type_enum",
        ...             values_callable=lambda x: [e.value for e in x],
        ...         ),
        ...         nullable=False,
        ...         index=True,
        ...     )
        >>>
        >>> # Создание контакта мобильного телефона
        >>> contact: Contact = Contact(value="89999999999", type=ContactType.PHONE)
        >>> # Создание контакта другого типа
        >>> contact_other: Contact = Contact(value="89999999999", type=ContactType.OTHER, other_type="Skype")
    """
    EMAIL = "0"
    PHONE = "1"
    VK = "2"
    SITE = "3"
    TELEGRAM = "4"
    WHATSAPP = "5"
    VIBER = "6"
    OTHER = "7"
