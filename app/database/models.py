from sqlalchemy.orm import Mapped, relationship

from database.config import *

# добавить alembic

# завод
class Factory(Base, PKMixin):
    name: Mapped[str_unique_nullable] 

# брэнд часов
class Brand(Base, PKMixin): 
    name: Mapped[str_unique_nullable]

# материал корпуса
class CaseMaterial(Base, PKMixin): 
    name: Mapped[str_unique_nullable]

# пол
class Gender(Base, PKMixin):
    name: Mapped[str_unique_nullable]

# функции механизмов
class Function(Base, PKMixin): 
    name: Mapped[str_unique_nullable]
    mechanism_functions: Mapped[list["MechanismFunction"]] = relationship("MechanismFunction", back_populates="function")

# тип механизма
class MechanismType(Base, PKMixin):
    name: Mapped[str_unique_nullable]

# пользователи
class User(Base, PKMixin, TimestampMixin): 
    name: Mapped[str_unique_nullable]
    email: Mapped[str_unique_nullable]
    oauth_provider: Mapped[str_nullable] 
    oauth_id: Mapped[str_unique_nullable]
    rating: Mapped[int_0_nullable]
    avito_url: Mapped[str | None]
    meshok_url: Mapped[str | None]

# механизмы
class Mechanism(Base, PKMixin, TimestampMixin):
    folder: Mapped[str_unique_nullable]
    stones: Mapped[int_nullable] 
    release: Mapped[int_nullable]
    
    code: Mapped[str_nullable]
    
    mechanism_type_id: Mapped[int] = Base.foreign_key_nullable(MechanismType)
    mechanism_type = relationship(MechanismType, lazy="joined")
    
    factory_id: Mapped[int] = Base.foreign_key_nullable(Factory)
    factory = relationship(Factory, lazy="joined")
    
    user_id: Mapped[int] = Base.foreign_key_nullable(User)
    user = relationship(User, lazy="joined")
    
    function_all: Mapped[list["MechanismFunction"]] = relationship("MechanismFunction", back_populates="mechanism", lazy="joined")
    

# несколько функций механизмов
class MechanismFunction(Base, PKMixin): 
    mechanism_id: Mapped[int] = Base.foreign_key_nullable(Mechanism)
    mechanism: Mapped[Mechanism] = relationship(Mechanism, back_populates="function_all", lazy="joined")
    
    function_id: Mapped[int] = Base.foreign_key_nullable(Function)
    function: Mapped[Function] = relationship(Function, back_populates="mechanism_functions", lazy="joined")
    

# часы
class Watch(Base, PKMixin, TimestampMixin):
    folder: Mapped[str_unique_nullable]
    code: Mapped[str | None]
    description: Mapped[str | None]
    integrated_bracelet: Mapped[bool_default_unique]
    start_release: Mapped[int_nullable]
    end_release: Mapped[int_nullable]
    
    gender_id: Mapped[int] = Base.foreign_key_nullable(Gender)
    gender = relationship(Gender, lazy="joined")
    
    case_material_id: Mapped[int] = Base.foreign_key_nullable(CaseMaterial)
    case_material = relationship(CaseMaterial, lazy="joined")
    
    mechanism_id: Mapped[int]  = Base.foreign_key_nullable(Mechanism)
    mechanism = relationship(Mechanism, lazy="joined")
    
    factory_id: Mapped[int] = Base.foreign_key_nullable(Factory)
    factory = relationship(Factory, lazy="joined")
    
    brand_id: Mapped[int] = Base.foreign_key_nullable(Brand)
    brand = relationship(Brand, lazy="joined")
    
    user_id: Mapped[int] = Base.foreign_key_nullable(User)
    user = relationship(User, lazy="joined")
    
    alias: Mapped[str | None]
    

# коллекция пользователя
class Collection(Base, PKMixin): 
    user_id: Mapped[int] = Base.foreign_key_nullable(User)
    watch_id: Mapped[int] = Base.foreign_key_nullable(Watch)

# аккаунты админов
class Admin(Base, PKMixin, TimestampMixin):
    name: Mapped[str_unique_nullable]
    password: Mapped[str_nullable] 

# заблокированные аккаунты 
class Blocked(Base, PKMixin, TimestampMixin):
    email: Mapped[str_unique_nullable]
    
# черновик - часы 
class DraftWatch(Base, PKMixin, TimestampMixin): 
    message: Mapped[str | None]
    folder: Mapped[str_unique_nullable]
    code: Mapped[int | None]
    integrated_bracelet: Mapped[bool_default_unique]
    start_release: Mapped[int | None]
    end_release: Mapped[int | None]
    gender_id: Mapped[int | None] = Base.foreign_key(Gender)
    case_material_id: Mapped[int | None] = Base.foreign_key(CaseMaterial)
    mechanism_id: Mapped[int | None]  =Base.foreign_key(Mechanism)
    factory_id: Mapped[int | None] = Base.foreign_key(Factory)
    brand_id: Mapped[int | None] = Base.foreign_key(Brand)
    user_id: Mapped[int] = Base.foreign_key(User)
    admin_id: Mapped[int | None] = Base.foreign_key(Admin)
    
# черновик - ключевые слова 
class DraftAlias(Base, PKMixin): 
    key: Mapped[str_nullable]
    watch_id: Mapped[int] = Base.foreign_key_nullable(Watch)
    
# черновик - механизмы
class DraftMechanism(Base, PKMixin, TimestampMixin):
    message: Mapped[str | None]
    folder: Mapped[str_unique_nullable]
    stones: Mapped[int | None] 
    start_release: Mapped[int | None]
    mechanism_type_id: Mapped[int | None] = Base.foreign_key(MechanismType)
    factory_id: Mapped[int | None] = Base.foreign_key(Factory)
    user_id: Mapped[int] = Base.foreign_key_nullable(User)
    admin_id: Mapped[int | None] = Base.foreign_key(Admin)

# черновик - несколько функций механизмов
class DraftMechanismFunction(Base, PKMixin):
    mechanism_id: Mapped[int] = Base.foreign_key_nullable(Mechanism)
    function_id: Mapped[int] = Base.foreign_key_nullable(Function)
    
    
