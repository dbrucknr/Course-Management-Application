from fastapi import FastAPI, Depends
# Local Imports
from config import settings, Settings
from lifespan import lifespan
from models import *

fastapi = FastAPI(lifespan=lifespan)

@fastapi.get("/")
async def index(settings: Settings = Depends(settings)):
    return settings