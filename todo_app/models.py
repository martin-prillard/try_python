"""Pydantic models (DTOs) and domain models.

Using Pydantic for validation and type-safety.
"""
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)


class TodoInDB(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool = False
    created_at: datetime


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    completed: Optional[bool] = None