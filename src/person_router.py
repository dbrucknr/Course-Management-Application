from fastapi import APIRouter, Depends
from functools import partial

from database import *

persons_router = APIRouter(prefix="/people", tags=["People"])


# GET: http://localhost:8000/people/?offset=0&limit=100
# http://localhost:8000/people/?offset=30&limit=100
# @persons_router.get(path="/", response_model=PaginatedResponse[PersonPublic])
# async def people(records: PaginatedResponse[Person] = Depends(partial(select_all_paginated, Person))):
#     return records

@persons_router.get(path="/students", response_model=PaginatedResponse[PublicStudent])
async def students(records: PaginatedResponse[Student] = Depends(partial(select_all_paginated, Student))):
    return records

@persons_router.get("/instructors", response_model=PaginatedResponse[PublicInstructor])
async def instructors(records: PaginatedResponse[Instructor] = Depends(partial(select_all_paginated, Instructor))):
    return records