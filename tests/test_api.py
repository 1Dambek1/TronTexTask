import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_wallet(async_client):
    response = await async_client.get("/tron/wallet?address=TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t")

    assert response.status_code == 200
    assert "balance" in response.json()

@pytest.mark.asyncio
async def test_wallet(async_client):
    response = await async_client.get("/tron/wallets?skip=0&limit=10&createdAtFilter=asc")

    assert response.status_code == 200
