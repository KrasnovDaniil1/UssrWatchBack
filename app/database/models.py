from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, text
from typing import Annotated
from database.config import Base
import datetime

# огранисения по строкам добавить
# добавить где данные могут быть пустые
#  почитать про Enum
# почитать про relationship
# добавить alembic
# добавить главного пользователя

def utc_now():
    return datetime.now(datetime.timezone.utc)

created_at = Annotated[
    datetime.datetime, 
    mapped_column(
        server_default = text("TIMEZONE('utc', now())"), 
        nullable=False
    )
] 

update_at = Annotated[
    datetime.datetime, 
    mapped_column(
        server_default = text("TIMEZONE('utc', now())"),
        onupdate = utc_now, 
        nullable=False
    )
]   

# -------- Часы --------

class Watch(Base): # часы
    __tablename__ = 'watch'
    id: Mapped[int] = mapped_column(primary_key=True)
    folder: Mapped[str] = mapped_column(unique=True, nullable=False)
    code: Mapped[int | None]
    integrated_bracelet: Mapped[bool] = mapped_column(default=False, nullable=False)
    gender_id: Mapped[int] = mapped_column(ForeignKey("gender.id"), nullable=False)
    case_material_id: Mapped[int] = mapped_column(ForeignKey("case_material.id"), nullable=False)
    mechanism_id: Mapped[int | None]  = mapped_column(ForeignKey("mechanism.id"))
    factory_id: Mapped[int | None] = mapped_column(ForeignKey("factory.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    created_at: Mapped[created_at]
    update_at:  Mapped[update_at]

class Factory(Base): # часовой завод
    __tablename__ = 'factory'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
class Alias(Base): # ключевые слова для часов
    __tablename__ = 'alias'
    id: Mapped[int] = mapped_column(primary_key=True)
    watch_id: Mapped[int] = mapped_column(ForeignKey("watch.id"), nullable=False)
    key: Mapped[str] = mapped_column(String(50), nullable=False)

class Brand(Base): # название брэнда часов
    __tablename__ = 'brand'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

class CaseMaterial(Base): # материал корпуса часов
    __tablename__ = 'case_material'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

class Gender(Base):
    __tablename__ = 'gender'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    

# -------- Механизмы --------


class Mechanism(Base): # механизмы
    __tablename__ = 'mechanism'
    id: Mapped[int] = mapped_column(primary_key=True)
    stones: Mapped[int | None] 
    mechanism_type_id: Mapped[int | None] = mapped_column(ForeignKey("mechanism_type.id"))
    factory_id: Mapped[int | None] = mapped_column(ForeignKey("factory.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    created_at: Mapped[created_at]
    update_at:  Mapped[update_at]
    
    
class Function(Base): # различные функции механизма
    __tablename__ = 'function'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

class MechanismFunction(Base): # соединение механизмов и функций
    __tablename__ = 'mechanism_function'
    id: Mapped[int] = mapped_column(primary_key=True)
    mechanism_id: Mapped[int] = mapped_column(ForeignKey("mechanism.id"), nullable=False)
    function_id: Mapped[int] = mapped_column(ForeignKey("function.id"), nullable=False)

class MechanismType(Base): # механизмы
    __tablename__ = 'mechanism_type'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)


# -------- Пользователь --------


class User(Base): # пользователь
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    login: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), nullable=False)
    avito_url: Mapped[str | None]
    meshok_url: Mapped[str | None]
    rating: Mapped[int | None]
    created_at: Mapped[created_at]
    update_at: Mapped[update_at]

class Role(Base): # роль пользователя
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

class Сollection(Base): # коллекция пользователя
    __tablename__ = 'collection'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    watch_id: Mapped[int] = mapped_column(ForeignKey("watch.id"), nullable=False)

# -------- Черновик с часами --------

class DraftWatch(Base): 
    __tablename__ = 'draft_watch'
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str | None]
    folder: Mapped[str] = mapped_column(unique=True)
    code: Mapped[int | None]
    integrated_bracelet: Mapped[bool] = mapped_column(default=False, nullable=False)
    gender_id: Mapped[int | None] = mapped_column(ForeignKey("gender.id"))
    case_material_id: Mapped[int | None] = mapped_column(ForeignKey("case_material.id"))
    mechanism_id: Mapped[int | None]  = mapped_column(ForeignKey("mechanism.id"))
    factory_id: Mapped[int | None] = mapped_column(ForeignKey("factory.id"))
    brand_id: Mapped[int | None] = mapped_column(ForeignKey("brand.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    created_at: Mapped[created_at]
    update_at:  Mapped[update_at]
    
class DraftAlias(Base): 
    __tablename__ = 'draft_alias'
    id: Mapped[int] = mapped_column(primary_key=True)
    watch_id: Mapped[int] = mapped_column(ForeignKey("watch.id"), nullable=False)
    key: Mapped[str] = mapped_column(String(50), nullable=False)
    
    
# -------- Черновик с механизмами --------


class DraftMechanism(Base):
    __tablename__ = 'draft_mechanism'
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str | None]
    stones: Mapped[int | None] 
    mechanism_type_id: Mapped[int | None] = mapped_column(ForeignKey("mechanism_type.id"))
    factory_id: Mapped[int | None] = mapped_column(ForeignKey("factory.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    created_at: Mapped[created_at]
    update_at:  Mapped[update_at]
    
class DraftMechanismFunction(Base):
    __tablename__ = 'draft_mechanism_function'
    id: Mapped[int] = mapped_column(primary_key=True)
    mechanism_id: Mapped[int] = mapped_column(ForeignKey("mechanism.id"), nullable=False)
    function_id: Mapped[int] = mapped_column(ForeignKey("function.id"), nullable=False)