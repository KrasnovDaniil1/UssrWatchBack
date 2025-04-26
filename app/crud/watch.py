from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import connection
from database.models import * 
from schemas.watch import GetWatch

@connection
async def get_all_watch(session: AsyncSession) -> list[GetWatch]:
    
    result = await session.execute(
        select(Watch)
        .options(
            selectinload(Watch.gender),
            selectinload(Watch.case_material),
            selectinload(Watch.brand),
            selectinload(Watch.alias_all)
        )
        )
    all_watch = result.scalars().all()
    watches = []

    for watch in all_watch:
        watches.append(GetWatch(
            id=watch.id,
            folder=watch.folder,
            start_release=watch.start_release,
            end_release=watch.end_release,
            gender=watch.gender.name,
            case_material=watch.case_material.name,
            brand=watch.brand.name,
            alias = [alias.key for alias in watch.alias_all]
        ))
    
    return watches