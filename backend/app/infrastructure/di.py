from fastapi import Depends
from app.repositories.health import HealthRepository
from app.usecases.health import HealthUseCase


def health_repository() -> HealthRepository:
    return HealthRepository()


def health_usecase(
    repo: HealthRepository = Depends(health_repository),
) -> HealthUseCase:
    return HealthUseCase(repo=repo)
