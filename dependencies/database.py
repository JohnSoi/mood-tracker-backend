"""Модуль зависимости подключения к БД"""

__author__: str = "Digital Horizons"

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import AsyncSessionLocal


async def get_session_db() -> AsyncSession:
    """
    Зависимость для получения сессии подключения к БД

    Returns:
        AsyncSession: сессия для асинхронной работы с БД

    Examples:
        >>> from fastapi import Depends
        >>>
        >>> from dependencies.database import AsyncSessionLocal
        >>>
        >>> def get_user(session_db: AsyncSession = Depends(get_session_db)):
        ...     ...

    Note:
        В конце каждого запроса сессия закрывается. В случае ошибки при выполнении запроса
        сессия откатывается автоматически
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()
