from uvicorn import run


if __name__ == "__main__":
    # Run FastAPI
    run(
        app='api.api:fastapi',
        host="0.0.0.0",
        port=8000,
        reload=True
    )