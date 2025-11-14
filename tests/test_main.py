import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_ping():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/ping")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_query_valid():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/query", json={
            "cadastral_number": "12-34-5678",
            "latitude": 55.75,
            "longitude": 37.62
        })
    assert r.status_code == 200
    data = r.json()
    assert data["cadastral_number"] == "12-34-5678"
    assert "result" in data

@pytest.mark.asyncio
async def test_query_invalid():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/query", json={
            "cadastral_number": "invalid123",
            "latitude": 95,   # неверная широта
            "longitude": 37.62
        })
    assert r.status_code == 422
