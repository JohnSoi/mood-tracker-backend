"""Модуль middleware для логера"""

__author__: str = "Digital Horizons"

import time
import uuid

from fastapi import Request, Response

from logger import app_logger


class LoggingMiddleware:
    """
    Middleware для логирования запросов в FastAPI

    Examples:
        >>> from fastapi import FastAPI
        >>> from logger import logging_middleware
        >>>
        >>> app: FastAPI = FastAPI()
        >>> @app.middleware("http")
        >>> async def add_logging_middleware(request: Request, call_next):
        >>>     return await logging_middleware(request, call_next)

setup_cors(app)


@app.middleware("http")
async def add_logging_middleware(request: Request, call_next):
    return await logging_middleware(request, call_next)
    """
    async def __call__(self, request: Request, call_next):
        # Генерируем ID запроса
        request_id: str = str(uuid.uuid4())

        # Засекаем время выполнения
        start_time: float = time.time()

        # Логируем входящий запрос
        app_logger.bind(
            http=True,
            request_id=request_id,
            method=request.method,
            url=str(request.url),
            client_host=request.client.host if request.client else None,
            user_agent=request.headers.get("user-agent")
        ).info("Incoming request")

        try:
            response: Response = await call_next(request)

            # Время выполнения
            process_time: float = time.time() - start_time

            # Логируем ответ
            app_logger.bind(
                http=True,
                request_id=request_id,
                method=request.method,
                url=str(request.url),
                status_code=response.status_code,
                process_time=round(process_time, 4)
            ).info("Request completed")

            # Добавляем ID запроса в заголовки ответа
            response.headers["X-Request-ID"] = request_id

            return response

        except Exception as exc:
            # Логируем ошибку
            process_time = time.time() - start_time

            app_logger.bind(
                http=True,
                request_id=request_id,
                method=request.method,
                url=str(request.url),
                process_time=round(process_time, 4),
                error_type=type(exc).__name__
            ).error(f"Request failed: {str(exc)}")

            raise


# Создаем экземпляр middleware
logging_middleware: LoggingMiddleware = LoggingMiddleware()
