from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from pydantic_settings import BaseSettings, SettingsConfigDict

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