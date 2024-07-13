from math import ceil
from typing import AsyncGenerator, Type
from fastapi import APIRouter, Depends, Query
from sqlmodel import select, func, text
from sqlmodel.ext.asyncio.session import AsyncSession
from main import database
from models import *
from schemas import PaginatedResponse
from functools import partial

persons_router = APIRouter(prefix="/people", tags=["People"])


async def count_records(model: Type[SQLModel], session: AsyncSession,) -> int:
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

# GET: http://localhost:8000/people/?offset=0&limit=100
# http://localhost:8000/people/?offset=30&limit=100
@persons_router.get(path="/", response_model=PaginatedResponse[PersonPublic])
async def people(records: PaginatedResponse[Person] = Depends(partial(select_all_paginated, Person))):
    return records

@persons_router.get(path="/students", response_model=PaginatedResponse[PublicStudent])
async def students(records: PaginatedResponse[Student] = Depends(partial(select_all_paginated, Student))):
    return records

@persons_router.get("/instructors", response_model=PaginatedResponse[PublicInstructor])
async def instructors(records: PaginatedResponse[Instructor] = Depends(partial(select_all_paginated, Instructor))):
    return records