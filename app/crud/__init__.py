from database import engine, async_session
from database.config import Base

from database.models import Factory, Brand, CaseMaterial, Gender, Function, MechanismType, Role
from database.seed_data import factory_seed, brand_seed, case_material_seed, gender_seed, function_seed, mechanism_type_seed, role_seed

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def seed_unique(session: AsyncSession, model, field_name: str, values: list[str]):
    for value in values:
        stmt = select(model).where(getattr(model, field_name) == value)
        result = await session.execute(stmt)
        exists = result.scalar_one_or_none()
        
        if not exists:
            session.add(model(**{field_name: value}))

    await session.commit()

# создание таблиц

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
async def create_data():        
    async with async_session() as session:
        await seed_unique(session, Factory, "name", factory_seed)
        await seed_unique(session, Brand, "name", brand_seed)
        await seed_unique(session, CaseMaterial, "name", case_material_seed)
        await seed_unique(session, Gender, "name", gender_seed)
        await seed_unique(session, Function, "name", function_seed)
        await seed_unique(session, MechanismType, "name", mechanism_type_seed)
        await seed_unique(session, Role, "name", role_seed)
        
    
