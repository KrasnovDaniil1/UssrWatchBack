from sqlalchemy import ForeignKey, text , Enum as SqlEnum
from sqlalchemy.orm import DeclarativeBase, class_mapper, mapped_column, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import expression

from typing import Type, Annotated

import datetime

from enum import Enum

# добавить alembic

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


class GenderEnum(str, Enum):
    WOMAN = "w"
    MAN = "m"
    ALL = "a"
    CHILDREN = "c"
class GenderMixin:
    gender: Mapped[GenderEnum] = mapped_column(
        SqlEnum(
            GenderEnum, 
            name="gender_enum", 
            validate_strings=True,
            native_enum=False,
            values_callable=lambda enum: [e.value for e in enum],
        ),
        nullable=False,
        default=GenderEnum.MAN,
        server_default=GenderEnum.MAN.value,
    )


class ProviderEnum(str, Enum):
    YANDEX = "y"
    GOOGLE = "g"
class ProviderMixin:
    provider: Mapped[ProviderEnum] = mapped_column(
        SqlEnum(
            ProviderEnum, 
            name="provider_enum", 
            validate_strings=True,
            native_enum=False,
            values_callable=lambda enum: [e.value for e in enum],
        ),
        nullable=False,
    )


str_unique_nullable = Annotated[
    str, 
    mapped_column(
        unique=True, 
        nullable=False
    )
] 


str_nullable = Annotated[
    str, 
    mapped_column(
        nullable=False
    )
] 


str_unique = Annotated[
    str | None, 
    mapped_column(
        unique=True, 
        nullable=True
    )
] 


int_nullable = Annotated[
    int, 
    mapped_column(
        nullable=False
    )
] 


bool_default_false = Annotated[
    bool, 
    mapped_column(
        default=False, 
        nullable=False,
        server_default=expression.literal('false')
    )
] 


bool_default_true = Annotated[
    bool, 
    mapped_column(
        default=True, 
        nullable=False,
        server_default=expression.literal('true')
    )
] 


int_default_0 = Annotated[
    int, 
    mapped_column(
        default=0, 
        nullable=False,
        server_default="0"
    )
] 


