import asyncio
from typing import AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient, AsyncHTTPTransport, WSGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from pathlib import Path
from pydantic_settings import BaseSettings
from pathlib import Path
from pydantic_settings import BaseSettings

from src.main import app
from src.db import DatabaseHelper
from src.models import BaseModel


BASE_DIR = Path(__file__).parent.parent


# DATABASE
class TestSettings(BaseSettings):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db_test.sqlite3"
    db_echo: bool = False


settings = TestSettings()

db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
# SETUP
transport = ASGITransport(app=app)
@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=transport,base_url="http://localhost:8000") as ac:
        yield ac
