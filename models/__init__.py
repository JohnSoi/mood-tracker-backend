"""Пакет моделей приложения"""

__author__: str = "Digital Horizons"

from .user import User as UserModel
from .access_data import AccessData as AccessDataModel
from .contact import Contact as ContactModel
from .friendship import FriendshipStatus as FriendshipStatusModel
from .session import Session as SessionModel
from .user_setting import UserSetting as UserSettingsModel
from .tags import Tag as TagModel
from .mood_entry import MoodEntry as MoodEntryModel
from .mood_entry_tags import MoodEntryTags as MoodEntryTagsModel
from .mood_entry_visibility import MoodEntryVisibility as MoodEntryVisibilityModel
