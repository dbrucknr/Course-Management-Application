from fastapi import APIRouter, Request, Depends, Query
from main import database

persons_router = APIRouter(prefix="/people", tags=["People"])

@persons_router.get("/")
async def get_people(request: Request):
    return {"message": "Hello, World!"}