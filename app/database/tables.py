from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, text
from typing import Annotated
import datetime

# огранисения по строкам добавить

def utc_now():
    return datetime.now(datetime.timezone.utc)

created_at = Annotated[
    datetime.datetime, 
    mapped_column(
        server_default = text("TIMEZONE('utc', now())")
    )
] 

update_at = Annotated[
    datetime.datetime, 
    mapped_column(
        server_default = text("TIMEZONE('utc', now())"),
        onupdate = utc_now
    )
]   

class Base(DeclarativeBase):
    pass

# -------- Часы --------

class Watch(Base): # часы
    __tablename__ = 'watch'
    id: Mapped[int] = mapped_column(primary_key=True)
    folder: Mapped[str] = mapped_column(unique=True)
    code: Mapped[int] = mapped_column(unique=True)
    integrated_bracelet: Mapped[bool]
    gender_id: Mapped[str] = mapped_column(ForeignKey("gender.id"))
    case_material_id: Mapped[int] = mapped_column(ForeignKey("case_material.id"))
    mechanism_id: Mapped[int]  = mapped_column(ForeignKey("mechanism.id"))
    factory_id: Mapped[int] = mapped_column(ForeignKey("factory.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[created_at]
    update_at:  Mapped[update_at]

class Factory(Base): # часовой завод
    __tablename__ = 'factory'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    
class Alias(Base): # ключевые слова для часов
    __tablename__ = 'alias'
    id: Mapped[int] = mapped_column(primary_key=True)
    watch_id: Mapped[int] = mapped_column(ForeignKey("watch.id"))
    key: Mapped[str]

class Brand(Base): # название брэнда часов
    __tablename__ = 'brand'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class CaseMaterial(Base): # материал корпуса часов
    __tablename__ = 'case_material'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class Gender(Base):
    __tablename__ = 'gender'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    

# -------- Механизмы --------


class Mechanism(Base): # механизмы
    __tablename__ = 'mechanism'
    id: Mapped[int] = mapped_column(primary_key=True)
    stones: Mapped[int | None] 
    mechanism_type_id: Mapped[str] = mapped_column(ForeignKey("mechanism_type.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[created_at]
    update_at:  Mapped[update_at]
    
    
class Function(Base): # различные функции механизма
    __tablename__ = 'function'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class MechanismFunction(Base): # соединение механизмов и функций
    __tablename__ = 'mechanism_function'
    id: Mapped[int] = mapped_column(primary_key=True)
    mechanism_id: Mapped[int] = mapped_column(ForeignKey("mechanism.id"))
    function_id: Mapped[int] = mapped_column(ForeignKey("function.id"))

class MechanismType(Base): # механизмы
    __tablename__ = 'mechanism_type'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)


# -------- Пользователь --------


class User(Base): # пользователь
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    role_id: Mapped[str] = mapped_column(ForeignKey("role.id"))
    avito_url: Mapped[str | None]
    meshok_url: Mapped[str | None]
    created_at: Mapped[created_at]
    update_at: Mapped[update_at]

class Role(Base): # роль пользователя
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class Сollection(Base): # коллекция пользователя
    __tablename__ = 'collection'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    watch_id: Mapped[int] = mapped_column(ForeignKey("watch.id"))
