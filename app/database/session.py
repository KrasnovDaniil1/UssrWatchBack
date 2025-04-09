from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings
# import asyncio

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True
)

# engine = create_engine(
#     url=settings.DATABASE_URL_asyncpg,
#     echo=True
# )

with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.all()}") 
    
# async def get_123():
#     async with engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"{res.all()}") 
        
# asyncio.run(get_123)