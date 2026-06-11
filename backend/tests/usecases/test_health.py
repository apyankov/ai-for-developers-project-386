import pytest
from app.domain.result import Success
from app.domain.objects import HealthObj
from app.usecases.health import HealthUseCase
from app.repositories.health import HealthRepository


@pytest.mark.asyncio
async def test_health_usecase_returns_success():
    use_case = HealthUseCase(repo=HealthRepository())
    result = await use_case()

    assert isinstance(result, Success)
    assert isinstance(result.data, HealthObj)
    assert result.data.status in ("ok", "degraded")
    assert result.data.version == "0.1.0"
    assert result.data.database in ("connected", "disconnected")
    assert result.data.uptime > 0


@pytest.mark.asyncio
async def test_health_api_returns_success(test_client):
    response = await test_client.get("/api/v1/health")

    assert response.status_code == 200
    body = response.json()
    assert body["type"] == "success"
    assert "data" in body
    assert body["data"]["status"] in ("ok", "degraded")
    assert body["data"]["version"] == "0.1.0"
    assert body["data"]["uptime"] > 0
