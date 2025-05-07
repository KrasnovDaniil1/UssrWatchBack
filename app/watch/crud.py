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
        selectinload(Watch.mechanism_type),
        selectinload(Watch.aliases),
        selectinload(Watch.gender),
    )
    
    if field.search_code:
        query = query.where(Watch.code == field.search_code)
    else:
        if field.gender:
            query = query.where(Watch.gender.has(Gender.name.in_(field.gender)))
        if field.brand:
            query = query.where(Watch.brand.has(Brand.name.in_(field.brand)))
        if field.case_material:
            query = query.where(Watch.case_material.has(CaseMaterial.name.in_(field.case_material)))
        if field.mechanism_type:
            query = query.where(Watch.mechanism_type.has(MechanismType.name.in_(field.mechanism_type)))
        if field.search_aliases:
            search_words = field.search_aliases.split()
            query = query.join(Watch.aliases)
            conditions = [
                WatchAlias.name.ilike(f"%{word}%") for word in search_words
            ]
            query = query.where(or_(*conditions)) 

    result = await session.execute(query)

    return [
        GetWatch(
            id = watch.id,
            folder = watch.folder,
            start_release = watch.start_release,
            end_release = watch.end_release,
            mechanism = watch.mechanism,
            gender = getattr(watch.gender, 'name', None),
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
            selectinload(Watch.factory),
            selectinload(Watch.gender),
            selectinload(Watch.mechanism_type)
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
        
        mechanism = watch.mechanism,
        code = watch.code,
        integrated_bracelet = watch.integrated_bracelet,
        width_bracelet = watch.width_bracelet,
        
        updated = watch.updated, 
        
        mechanism_type = getattr(watch.mechanism_type, 'name', None),
        gender = getattr(watch.gender, 'name', None),
        case_material = getattr(watch.case_material, 'name', None),
        brand = getattr(watch.brand, 'name', None),
        factory = getattr(watch.factory, 'name', None),
        
        functions = [wf.function.name for wf in watch.functions],
        aliases = [a.name for a in watch.aliases],

    )
