# Python Dependencies
from typing import AsyncGenerator, Any
from contextlib import asynccontextmanager
# FastAPI Dependencies
from fastapi import FastAPI
# Local Dependencies
from database import database
from generate_data import *

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[Any, None]:
    """
        Lifespan event handler for FastAPI application.

        On start: Create all tables in the database.
        On stop: Drop all tables in the database.
    """
    await database.create_all_tables()
    initialized = await check_if_data_exists()
    if not initialized:
        await create_fake_data()
    yield
    # await database.drop_all_tables()