from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI
from pymongo import AsyncMongoClient

from core.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    client = AsyncMongoClient(settings.MONGO_CONNECTION_STRING)
    database = client.todoapp

    await init_beanie(database=database, document_models=[])

    try:
        yield
    finally:
        await client.close()


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)
