# Python Dependencies
from typing import AsyncGenerator
# SQLModel
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
# SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
# Local Dependencies
from config import settings

class AsyncDatabase:
    def __init__(self) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=str(settings().DATABASE_URI),
            echo=True, 
            future=True
        )
        self.SessionLocal: AsyncSession = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.SessionLocal() as session:
            yield session

    async def create_all_tables(self):
        async with self.engine.begin() as connection:
            await connection.run_sync(SQLModel.metadata.create_all)

    async def drop_all_tables(self):
        async with self.engine.begin() as connection:
            await connection.run_sync(SQLModel.metadata.drop_all)