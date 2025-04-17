from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from app.database.config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg
    )

async_session_maker = async_sessionmaker(
    engine, 
    expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True 

