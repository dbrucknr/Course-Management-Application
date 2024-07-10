from fastapi import FastAPI, Depends
# Local Imports
from config import settings, Settings

fastapi = FastAPI()

@fastapi.get("/")
async def index(settings: Settings = Depends(settings)):
    return settings