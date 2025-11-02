from enum import StrEnum


class MoodEntryPublishStatus(StrEnum):
    """
    Типы статусов записи настроения

    Attributes:
        FOR_ME (str): только для себя
        ONLY_FRIENDS (str): только для друзей
        ONLY_USER (str): только для конкретных людей
        ONLY_FRIEND_EXCLUDED_USER (str): исключить конкретных людей
        FOR_ALL_EXCLUDED_USER (str): исключить конкретных людей
        FOR_ALL (str): публичная запись

    Examples:
        >>> publish_status: MoodEntryPublishStatus = MoodEntryPublishStatus.FOR_ME
        >>>
        >>> def visible_for_user(status: MoodEntryPublishStatus) -> bool:
        >>>     return status == MoodEntryPublishStatus.ONLY_FRIENDS or status == MoodEntryPublishStatus.FOR_ALL
        >>>
        >>> print(visible_for_user(publish_status)) # False - видит только пользователь
    """
    FOR_ME = "for_me"
    ONLY_FRIENDS = "only_friends"
    ONLY_USER = "only_user"
    ONLY_FRIEND_EXCLUDED_USER = "only_friend_excluded_user"
    FOR_ALL_EXCLUDED_USER = "for_all_excluded_user"
    FOR_ALL = "for_all"
