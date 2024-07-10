from uvicorn import run
from database import AsyncDatabase

database = AsyncDatabase()

if __name__ == "__main__":
    # Run FastAPI
    run(
        app='api:fastapi',
        host="0.0.0.0",
        port=8000,
        reload=True
    )