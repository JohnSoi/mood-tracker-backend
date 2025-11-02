from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app: FastAPI = FastAPI()


@app.get("/")
def read_root():
    """Редирект на страницу документации"""
    return RedirectResponse(url="/docs")
