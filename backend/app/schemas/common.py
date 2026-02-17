from pydantic import BaseModel, Field, validator
from typing import Optional, List


class PaginationParams(BaseModel):
    skip: int = Field(0, ge=0)
    limit: int = Field(100, gt=0, le=1000)


class ErrorResponse(BaseModel):
    detail: str
    status_code: int
    timestamp: str


class SuccessResponse(BaseModel):
    message: str
    data: Optional[dict] = None


class DashboardStats(BaseModel):
    total_users: int = Field(..., ge=0)
    active_users: int = Field(..., ge=0)
    total_sessions: int = Field(..., ge=0)
    cpu_usage: float = Field(..., ge=0, le=100)
    memory_usage: float = Field(..., ge=0, le=100)
