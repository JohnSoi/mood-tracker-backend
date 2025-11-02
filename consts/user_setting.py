from enum import StrEnum

MAX_LENGTH_NAME_AND_VALUE: int = 50
MAX_TYPE_LENGTH: int = 10
DEFAULT_TYPE: str = "str"


class UserSettingType(StrEnum):
    """
    Базовые типы параметров пользователей

    Attributes:
        STR (str): строка
        INT (str): целое число
        FLOAT (str): вещественное число
        BOOL (str): флаг

    Examples:
        >>> user_param_type: str = "bool"
        >>> is_bool: bool = user_param_type == UserSettingType.BOOL # True
        >>> is_str: bool = user_param_type == UserSettingType.STR # False
    """

    STR = "str"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
