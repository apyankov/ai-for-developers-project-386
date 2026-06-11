from collections.abc import AsyncGenerator
import pytest_asyncio
from testcontainers.mongodb import MongoDbContainer
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.infrastructure.database import Database


@pytest_asyncio.fixture(scope="session")
async def mongodb_container():
    with MongoDbContainer("mongo:7") as container:
        container.start()
        yield container


@pytest_asyncio.fixture
async def test_client(mongodb_container) -> AsyncGenerator[AsyncClient, None]:
    uri = mongodb_container.get_connection_url()
    import os
    os.environ["MONGO_URI"] = uri

    await Database.connect()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
    await Database.disconnect()
