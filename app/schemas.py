from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class QueryCreate(BaseModel):
    cadastral_number: str = Field(..., min_length=1)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    @validator("cadastral_number")
    def check_cadastral_number(cls, v):
        if not v.replace("-", "").isdigit():
            raise ValueError("Кадастровый номер должен содержать только цифры и дефисы")
        return v

class QueryResponse(BaseModel):
    id: int
    cadastral_number: str
    latitude: float
    longitude: float
    result: Optional[bool]
    created_at: datetime

    class Config:
        orm_mode = True
