from pydantic_settings import BaseSettings, SettingsConfigDict

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import DeclarativeBase, class_mapper, mapped_column, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr

from typing import Type, Annotated

import datetime

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

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True 
    
    def to_dict(self) -> dict:
        columns = class_mapper(self.__class__).columns
        return {column.key: getattr(self, column.key) for column in columns}
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    
    @staticmethod
    def foreign_key(table_class: Type) -> ForeignKey:
        return mapped_column(ForeignKey(f"{table_class.__tablename__}.id"))
    
    @staticmethod
    def foreign_key_nullable(table_class: Type) -> ForeignKey:
        return mapped_column(ForeignKey(f"{table_class.__tablename__}.id"), nullable=False)
    

def utc_now():
    return datetime.now(datetime.timezone.utc)

class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default = text("TIMEZONE('utc', now())"), 
        nullable = False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default = text("TIMEZONE('utc', now())"), 
        onupdate = utc_now, 
        nullable = False
    )

class PKMixin:
    @declared_attr
    def id(cls) -> Mapped[int]:
        return mapped_column(primary_key=True)
    
str_unique_nullable = Annotated[
    str, 
    mapped_column(unique=True, nullable=False)
] 

str_nullable = Annotated[
    str, 
    mapped_column(nullable=False)
] 

str_unique = Annotated[
    str, 
    mapped_column(unique=True)
] 

int_nullable = Annotated[
    int, 
    mapped_column(nullable=False)
] 

bool_default_unique = Annotated[
    bool, 
    mapped_column(default=False, nullable=False)
] 

int_0_nullable = Annotated[
    int, 
    mapped_column(default=0, nullable=False)
] 


