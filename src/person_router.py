from fastapi import APIRouter, Depends, Query
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from main import database
from models import *

persons_router = APIRouter(prefix="/people", tags=["People"])

@persons_router.get("/")
async def people(
    session: AsyncSession = Depends(database.get_session),
    offset: int = 0, 
    limit: int = Query(default=100, le=100)
):
    statement = select(Person).offset(offset).limit(limit)
    result = await session.exec(statement)
    people = result.all()
    return people

@persons_router.get("/students")
async def students():
    return {"message": "Hello, World!"}

@persons_router.get("/")
async def instructors():
    return {"message": "Hello, World!"}