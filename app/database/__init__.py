from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from database.config import settings

engine = create_async_engine(
    url = settings.DATABASE_URL_asyncpg,
    echo = False                                                            
)
async_session = async_sessionmaker(
    engine, 
    expire_on_commit=False
)

def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            try:
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()  
                raise e  
            finally:
                await session.close()  

    return wrapper