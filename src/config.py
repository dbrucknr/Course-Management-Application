from pydantic_settings import BaseSettings
from pydantic_core import MultiHostUrl
from pydantic import computed_field

from functools import lru_cache
from logging import getLogger

log = getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "development"
    testing: bool = False

    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""
    POSTGRES_SERVER: str

    @computed_field
    @property
    def DATABASE_URI(self) -> MultiHostUrl:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=f"{self.POSTGRES_DB}",
        )

@lru_cache()
def settings() -> Settings:
    log.info("Loading settings from the environment...")
    return Settings()