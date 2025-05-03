from fastapi import FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, async_session
from database.base import Base
from database.model import *
from database.seed_data import *
from database.test_data import *

async def start_db(app: FastAPI):
    await create_db()
    await add_seed()
    await add_test()
    yield

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) # ! убрать
        await conn.run_sync(Base.metadata.create_all)
        
async def add_seed():        
    async with async_session() as session:
        await seed_unique(session, Factory, "name", factory)
        await seed_unique(session, Brand, "name", brand)
        await seed_unique(session, CaseMaterial, "name", case_material)
        await seed_unique(session, Function, "name", function)
        await seed_unique(session, MechanismType, "name", mechanism_type)
        await seed_admin(session, Admin, "login", admin)

async def add_test(): # ! убрать
    async with async_session() as session:
        await seed_test(session, User,  user_test)
        await seed_test(session, Mechanism, mechanism_test)
        await seed_test(session, MechanismFunction, mechanism_function_test)
        await seed_test(session, Watch, watch_test)
        await seed_test(session, DraftWatch, draft_watch_test)
        await seed_test(session, DraftAlias, draft_alias_test)
        await seed_test(session, DraftMechanism, draft_mechanism_test)
        await seed_test(session, DraftMechanismFunction, draft_mechanism_function_test)
        
        
async def seed_unique(session: AsyncSession, model, field_name: str, values: list[str]):
    for value in values:
        stmt = select(model).where(getattr(model, field_name) == value)
        result = await session.execute(stmt)
        if result.scalar_one_or_none() is None:
            session.add(model(**{field_name: value}))
    await session.commit()
    
async def seed_admin(session: AsyncSession, model, field_name: str, values: list[dict]):
    for value in values:
        stmt = select(model).where(getattr(model, field_name) == value[field_name])
        result = await session.execute(stmt)
        if result.scalar_one_or_none() is None:
            session.add(model(**value))
    await session.commit()

async def seed_test(session: AsyncSession, model, values: list[dict]):
    session.add_all([model(**value) for value in values])
    await session.commit()
        
    
