from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from database.session import Base

# посмотреть как делать уникальные значения
# как вести документацию по таблицам
# сделать цвет корпуса
# добавить счетчик гейгера

# -------- Часы --------

class Watch(Base): # часы
    __tablename__ = 'watch'
    id: Mapped[int] = mapped_column(primary_key=True)
    folder: Mapped[str]
    watch_gender_id: Mapped[str] = mapped_column(ForeignKey("watch_gender.id"))
    case_material_id: Mapped[int] = mapped_column(ForeignKey("case_material.id"))
    mechanism_id: Mapped[int]  = mapped_column(ForeignKey("mechanism.id"))
    watch_factory_id: Mapped[int] = mapped_column(ForeignKey("watch_factory.id"))
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    integrated_bracelet: Mapped[bool]

class WatchFactory(Base): # часовой завод
    __tablename__ = 'watch_factory'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class WatchAliases(Base): # ключевые слова для часов
    __tablename__ = 'aliases'
    id: Mapped[int] = mapped_column(primary_key=True)
    watch_id: Mapped[int] = mapped_column(ForeignKey("watch.id"))
    key: Mapped[str]

class WatchBrand(Base): # название брэнда часов
    __tablename__ = 'brand'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class WatchCaseMaterial(Base): # материал корпуса часов
    __tablename__ = 'case_material'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 

class WatchGender(Base):
    __tablename__ = 'watch_gender'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    


# -------- Механизмы --------



class Mechanism(Base): # механизмы
    __tablename__ = 'mechanism'
    id: Mapped[int] = mapped_column(primary_key=True)
    stones: Mapped[int | None] 
    type: Mapped[str] = mapped_column(ForeignKey("mechanism_type.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
class Functions(Base): # различные функции механизма
    __tablename__ = 'functions'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] #automatic|winding|shockproof|chronograph|stop|moon|dayweek|day

class MechanismFunctions(Base): # соединение механизмов и функций
    __tablename__ = 'mechanism_functions'
    id: Mapped[int] = mapped_column(primary_key=True)
    mechanism_id: Mapped[int] = mapped_column(ForeignKey("mechanism.id"))
    functions_id: Mapped[int] = mapped_column(ForeignKey("functions.id"))

class MechanismType(Base): # механизмы
    __tablename__ = 'mechanism_type'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] # Механические|Кварцевые



# -------- Пользователь --------



class Users(Base): # пользователь
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    role: Mapped[str] # admin|user|ban
    
class Сollection(Base): # коллекция пользователя
    __tablename__ = 'collection'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    watch_id: Mapped[int]
