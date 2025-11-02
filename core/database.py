"""Модуль для работы с базой данных"""

__author__: str = "Digital Horizons"

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)

from core.config import settings

# Экземпляр подключения к БД
engine: AsyncEngine = create_async_engine(str(settings.DB_URL), echo=settings.DEBUG)

# Мейкер сессий для подключения к БД
AsyncSessionLocal: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
