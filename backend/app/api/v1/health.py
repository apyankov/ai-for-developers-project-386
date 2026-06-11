from fastapi import APIRouter, Depends

from app.domain.result import Success, Failure
from app.domain.dto import HealthDto
from app.usecases.health import HealthUseCase
from app.infrastructure.di import health_usecase

router = APIRouter(tags=["health"])


@router.get("/api/v1/health")
async def get_health(
    use_case: HealthUseCase = Depends(health_usecase),
) -> Success[HealthDto] | Failure:
    return await use_case()
