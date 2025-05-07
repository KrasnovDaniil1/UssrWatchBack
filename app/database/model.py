from sqlalchemy.orm import Mapped, relationship

from database.base import *

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

# функции часов
class Function(Base, PKMixin): 
    name: Mapped[str_unique_nullable]

# тип механизма
class MechanismType(Base, PKMixin):
    name: Mapped[str_unique_nullable]

# часы
class Watch(Base, PKMixin, TimestampMixin, GenderMixin):
    folder: Mapped[str_unique_nullable]
    code: Mapped[str | None]
    start_release: Mapped[int | None]
    end_release: Mapped[int | None]
    mechanism: Mapped[str | None]
    integrated_bracelet: Mapped[bool_default_false]
    description: Mapped[str | None]
    width_bracelet: Mapped[int | None]
    
    case_material_id: Mapped[int | None] = Base.foreign_key(CaseMaterial)
    case_material = relationship(CaseMaterial, lazy="joined")
    
    factory_id: Mapped[int | None] = Base.foreign_key(Factory)
    factory = relationship(Factory, lazy="joined")
    
    brand_id: Mapped[int | None] = Base.foreign_key(Brand)
    brand = relationship(Brand, lazy="joined")

    functions = relationship("WatchFunction", back_populates="watch_function", lazy="joined")
    
    aliases = relationship("WatchAlias", back_populates="watch_alias", lazy="joined")

class WatchAlias(Base, PKMixin): 
    watch_id: Mapped[int] = Base.foreign_key_nullable(Watch)
    name: Mapped[str_nullable]
    
    watch_alias = relationship(Watch, back_populates="aliases")

class WatchFunction(Base, PKMixin): 
    watch_id: Mapped[int] = Base.foreign_key_nullable(Watch)
    function_id: Mapped[int] = Base.foreign_key_nullable(Function)
    
    watch_function = relationship("Watch", back_populates="functions")
    function = relationship("Function", lazy="joined")
    


    

