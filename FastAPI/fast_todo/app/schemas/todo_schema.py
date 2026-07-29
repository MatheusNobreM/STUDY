from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class TodoCreate(BaseModel):
    title: str = Field(..., title="Titulo", min_length=3, max_length=20)
    description: str = Field(..., title="Description", min_lenght=3, max_length=50)
    status: Optional[bool] = False


class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str] = False


class TodoDetail(BaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
