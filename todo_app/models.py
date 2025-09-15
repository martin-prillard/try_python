"""Pydantic models (DTOs) and domain models.

Using Pydantic for validation and type-safety.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)


class TodoInDB(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False
    created_at: datetime


class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    completed: bool | None = None
