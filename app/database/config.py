from pydantic_settings import BaseSettings, SettingsConfigDict

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

# добавить alembic
# добавить таблицы для черновиков

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")
    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
settings = Settings()

DATABASE_URL = settings.DATABASE_URL_asyncpg

engine = create_async_engine(
    url = DATABASE_URL,
    echo = False                                                            
)
async_session = async_sessionmaker(
    engine, 
    expire_on_commit=False
)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True 



