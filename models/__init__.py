"""Пакет моделей приложения"""

__author__: str = "Digital Horizons"

from .user import User as UserModel
from .access_data import AccessData as AccessDataModel
from .contact import Contact as ContactModel
from .friendship import FriendshipStatus as FriendshipStatusModel
from .session import Session as SessionModel