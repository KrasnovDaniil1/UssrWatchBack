from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import connection
from database.models import Brand

@connection
async def create_brand(name: str, session: AsyncSession) -> int:
    brand = Brand(name=name)
    session.add(brand)
    await session.commit()
    return brand.id

@connection
async def select_all_brand(session: AsyncSession) -> int:
    query = select(Brand)
    result = await session.execute(query)
    records = result.scalars().all()
    return records

# @connection
# async def update_brand(name:str, new_name: str, session: AsyncSession) -> int:
#     brand = Brand(name=name)
#     session.add(brand)
#     await session.commit()
#     return brand.id
