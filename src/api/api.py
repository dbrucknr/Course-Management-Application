from fastapi import FastAPI, Depends
# Local Imports
from config import settings, Settings
from api.lifespan import lifespan
from database.models import *

from api.modules.person.router import router as person_router
from api.modules.student.router import router as student_router
from api.modules.instructor.router import router as instructor_router

from person_router import persons_router

fastapi = FastAPI(lifespan=lifespan)
# fastapi.include_router(persons_router)
fastapi.include_router(router=person_router)
fastapi.include_router(router=student_router)
fastapi.include_router(router=instructor_router)

@fastapi.get("/")
async def index(settings: Settings = Depends(settings)):
    return settings