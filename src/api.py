from fastapi import FastAPI

fastapi = FastAPI()

@fastapi.get("/")
async def index():
    return {"message": "Hello, World!"}