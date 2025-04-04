import pytest
from httpx import AsyncClient
from src.app import app

@pytest.fixture
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_wallet(async_client):
    response = await async_client.get("/tron/wallet?address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t")
    assert response.status_code == 200
