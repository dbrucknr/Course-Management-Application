from fastapi import FastAPI, Depends
# Local Imports
from config import settings, Settings
from lifespan import lifespan
from database.models import *
from person_router import persons_router

fastapi = FastAPI(lifespan=lifespan)
fastapi.include_router(persons_router)

@fastapi.get("/")
async def index(settings: Settings = Depends(settings)):
    return settings