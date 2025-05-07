from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload

from database import connection
from database.model import * 

from watch.schema import *

@connection
async def get_watch_all(field: GetWatchField, session: AsyncSession) -> list[GetWatch]:
    
    query = select(Watch).options(
        selectinload(Watch.case_material),
        selectinload(Watch.brand),
        selectinload(Watch.aliases),
    )
    
    if field.search_code:
        query = query.where(Watch.code == field.search_code)
    else:
        if field.brand:
            query = query.where(Watch.brand.has(name = field.brand))
        if field.gender:
            query = query.where(Watch.gender == field.gender)
        if field.case_material:
            query = query.where(Watch.case_material.has(name = field.case_material))
        if field.search_aliases:
            search_words = field.search_aliases.split()
            query = query.join(Watch.aliases)
            conditions = [
                WatchAlias.alias.ilike(f"%{word}%") for word in search_words
            ]
            query = query.where(or_(*conditions)) 

    result = await session.execute(query)

    return [
        GetWatch(
            id = watch.id,
            folder = watch.folder,
            start_release = watch.start_release,
            end_release = watch.end_release,
            gender = watch.gender,
            mechanism = watch.mechanism,
            case_material = getattr(watch.case_material, 'name', None),
            brand = getattr(watch.brand, 'name', None),
            aliases = [a.name for a in watch.aliases]
        )
        for watch in result.unique().scalars().all()
    ]

@connection
async def get_watch_by_id(id: int, session: AsyncSession) -> GetWatchId | None:
    
    result = await session.execute(
        select(Watch)
        .options(
            selectinload(Watch.case_material),
            selectinload(Watch.brand),
            selectinload(Watch.functions),
            selectinload(Watch.aliases),
            selectinload(Watch.factory)
            
        ).where(Watch.id == id)
    )
        
    watch = result.unique().scalar_one_or_none()

    if watch is None:
        return None

    return GetWatchId(
        id=watch.id,
        folder=watch.folder,
        start_release=watch.start_release,
        end_release=watch.end_release,
        gender=watch.gender,
        case_material = getattr(watch.case_material, 'name', None),
        brand = getattr(watch.brand, 'name', None),
        mechanism = watch.mechanism,
        code = watch.code,
        integrated_bracelet = watch.integrated_bracelet,
        width_bracelet = watch.width_bracelet,
        
        factory = getattr(watch.factory, 'name', None),
        
        functions = [wf.function.name for wf in watch.functions],
        aliases = [a.name for a in watch.aliases],

        updated = watch.updated,  
    )
