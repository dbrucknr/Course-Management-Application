from math import ceil
from typing import AsyncGenerator, Type
from fastapi import Depends, Query
from sqlmodel import SQLModel, select, func
from sqlmodel.ext.asyncio.session import AsyncSession

from main import database
from .schemas import PaginatedResponse

async def count_records(model: Type[SQLModel], session: AsyncSession) -> int:
    count_statement = select(func.count()).select_from(model)
    count_result = await session.exec(count_statement)
    total_count = count_result.one()
    return total_count

async def select_all_paginated(
    model: Type[SQLModel], 
    offset: int = 1,
    limit: int = Query(default=100, le=100),
    session: AsyncSession = Depends(database.get_session),
) -> AsyncGenerator[PaginatedResponse, None]:
    
    record_count = await count_records(model, session)
    skip = (offset - 1) * limit
    statement = select(model).offset(skip).limit(limit)
    result = await session.exec(statement)

    yield PaginatedResponse(
        current_page=offset,
        total_pages=ceil(record_count / limit),
        count=record_count, 
        data=result.all()
    )