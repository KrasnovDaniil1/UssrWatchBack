from database import engine, async_session
from database.config import Base

from database.models import *
from database.seed_data import *
from database.test_data import *


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import FastAPI


# создание таблиц и промежуточных данных
async def start_db(app: FastAPI):
    await create_db()
    await create_data()
    yield

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) # ! убрать
        await conn.run_sync(Base.metadata.create_all)
        
async def create_data():        
    async with async_session() as session:
        await seed_unique(session, Factory, "name", factory_seed)
        await seed_unique(session, Brand, "name", brand_seed)
        await seed_unique(session, CaseMaterial, "name", case_material_seed)
        await seed_unique(session, Gender, "name", gender_seed)
        await seed_unique(session, Function, "name", function_seed)
        await seed_unique(session, MechanismType, "name", mechanism_type_seed)
        await seed_admin(session, Admin, "name", admin_seed)
    
        await seed_other(session, User,  user_test)
        await seed_other(session, Mechanism, mechanism_test)
        await seed_other(session, MechanismFunction, mechanism_function_test)
        await seed_other(session, Watch, watch_test)
        await seed_other(session, Alias, alias_test)
        await seed_other(session, Collection, collection_test)
        await seed_other(session, Blocked, blocked_test)
        await seed_other(session, DraftWatch, draft_watch_test)
        await seed_other(session, DraftAlias, draft_alias_test)
        await seed_other(session, DraftMechanism, draft_mechanism_test)
        await seed_other(session, DraftMechanismFunction, draft_mechanism_function_test)
        
        
async def seed_unique(session: AsyncSession, model, field_name: str, values: list[str]):
    for value in values:
        stmt = select(model).where(getattr(model, field_name) == value)
        result = await session.execute(stmt)
        exists = result.scalar_one_or_none()
        
        if not exists:
            session.add(model(**{field_name: value}))

    await session.commit()
    
async def seed_admin(session: AsyncSession, model,  field_name: str, values: list[dict]):
    for value in values:
        stmt = select(model).where(getattr(model, field_name) == value["name"])
        result = await session.execute(stmt)
        exists = result.scalar_one_or_none()
        
        if not exists:
            session.add(model(**value))

    await session.commit()

async def seed_other(session: AsyncSession, model, values: list[dict]):
    for value in values:
        session.add(model(**value))

    await session.commit()
        
    
