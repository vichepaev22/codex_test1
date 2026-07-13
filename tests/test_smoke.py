import asyncio

import httpx

from app.main import app


async def request(path: str) -> httpx.Response:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://testserver",
    ) as client:
        return await client.get(path)


def test_root_reports_service_status() -> None:
    response = asyncio.run(request("/"))

    assert response.status_code == 200
    assert response.json() == {
        "service": "loop-engineering-sandbox",
        "status": "ok",
    }


def test_health_endpoint() -> None:
    response = asyncio.run(request("/health"))

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
