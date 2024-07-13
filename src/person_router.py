from math import ceil
from fastapi import APIRouter, Depends, Query
from sqlmodel import select, func
from sqlmodel.ext.asyncio.session import AsyncSession
from main import database
from models import *
from schemas import PaginatedResponse

persons_router = APIRouter(prefix="/people", tags=["People"])

# GET: http://localhost:8000/people/?offset=0&limit=100
# http://localhost:8000/people/?offset=30&limit=100
@persons_router.get("/", response_model=PaginatedResponse[PersonPublic])
async def people(
    session: AsyncSession = Depends(database.get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100)
):
    skip = (offset - 1) * limit

    count_statement = select(func.count(Person.id))
    count_result = await session.exec(count_statement)
    total_count = count_result.one()

    statement = select(Person).offset(skip).limit(limit)
    result = await session.exec(statement)
    people = result.all()

    return PaginatedResponse(
        current_page=offset,
        total_pages=ceil(total_count / limit),
        count=total_count, 
        data=people
    )

@persons_router.get(
    "/students", 
    response_model=list[PublicStudent]
)
async def students(
    session: AsyncSession = Depends(database.get_session),
    offset: int = 0, 
    limit: int = Query(default=100, le=100)
):
    statement = select(Student).offset(offset).limit(limit)
    result = await session.exec(statement)
    students = result.all()
    return students

@persons_router.get("/instructors")
async def instructors(
    session: AsyncSession = Depends(database.get_session),
    offset: int = 0, 
    limit: int = Query(default=100, le=100)
):
    statement = select(Instructor).offset(offset).limit(limit)
    result = await session.exec(statement)
    instructors = result.all()
    return instructors