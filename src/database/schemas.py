from pydantic import BaseModel
from sqlmodel import SQLModel
from typing import Generic, TypeVar

T = TypeVar('T', bound=SQLModel)

class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated Response"""
    current_page: int
    total_pages: int
    count: int
    data: list[T]