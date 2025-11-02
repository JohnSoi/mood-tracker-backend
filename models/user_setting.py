from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from consts.user_setting import (
    MAX_LENGTH_NAME_AND_VALUE,
    MAX_TYPE_LENGTH,
    DEFAULT_TYPE,
    UserSettingType,
)
from .base import BaseModel
from .user import User


class UserSetting(BaseModel):
    """
    Модель для настроек пользователя

    Attributes:
        name (str): название параметра
        value (str): значение параметра
        type (str): тип параметра. Если тип параметра совпадает с базовыми - значение можно получить через
        formatted_value. Если тип другой - преобразование остается за прикладным разработчиком
        user_id (int | None): идентификатор связанного пользователя. Параметры без него считаются общими
        user (UserModel | None): данные о связанном пользователе
    """

    name: Mapped[str] = mapped_column(
        String(MAX_LENGTH_NAME_AND_VALUE), index=True, nullable=False
    )
    value: Mapped[str] = mapped_column(
        String(MAX_LENGTH_NAME_AND_VALUE), nullable=False
    )
    type: Mapped[str] = mapped_column(
        String(MAX_TYPE_LENGTH), nullable=False, default=DEFAULT_TYPE
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), index=True, nullable=True
    )

    user: Mapped["User"] = relationship("User")

    @property
    def formatted_value(self) -> str | bool | int | float:
        """
        Получение форматированного значения

        Returns:
            (str | bool | int | float): значение сохраненного типа, если он присутствует в базовых - иначе строка

        Examples:
            >>> settings_int: UserSetting = UserSetting(value=str(5), type=UserSettingType.INT)
            >>> settings_int.formatted_value # 5
            >>> settings_bool: UserSetting = UserSetting(value=str(True), type=UserSettingType.BOOL)
            >>> settings_bool.formatted_value # True
            >>> # тип кастомный - преобразует сам прикладник
            >>> settings_list: UserSetting = UserSetting(value=str([1, 2, 3]), type="list")
            >>> settings_list.formatted_value # '[1, 2, 3]'
        """
        match self.type:
            case UserSettingType.BOOL:
                return self.value == str(True)
            case UserSettingType.INT:
                return int(self.value)
            case UserSettingType.FLOAT:
                return float(self.value)
            case _:
                return self.value
