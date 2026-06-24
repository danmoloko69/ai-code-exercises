from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class TodoStatus(str, Enum):
    pending = "pending"
    completed = "completed"


class TodoBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="A short title for the to-do item",
    )
    description: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="A detailed description of the to-do item",
    )
    due_date: date = Field(
        ..., description="The due date for this item in YYYY-MM-DD format"
    )


class TodoCreate(TodoBase):
    """Model for creating a new to-do item."""


class TodoResponse(TodoBase):
    id: int = Field(..., description="Unique ID assigned to the to-do item")
    status: TodoStatus = Field(
        TodoStatus.pending,
        description="Current status of the to-do item",
    )

    class Config:
        orm_mode = True
