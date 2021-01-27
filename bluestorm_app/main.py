from fastapi import FastAPI

from .routes import search_router

app = FastAPI(
    title="Bluestorm Challenge",
    description="REST API create for the challenge proposed by Bluestorm",
    version="1.0",
)

app.include_router(search_router)