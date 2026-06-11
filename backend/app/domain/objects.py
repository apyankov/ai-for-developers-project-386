from pydantic import BaseModel


class HealthObj(BaseModel):
    status: str
    version: str
    database: str
    uptime: float
