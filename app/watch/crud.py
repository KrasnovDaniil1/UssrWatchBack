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
        selectinload(Watch.mechanism),
        selectinload(Watch.user),
    )
    
    if field.search_code:
        query = query.where(Watch.code == field.search_code)
    else:
        if field.brand:
            query = query.where(Watch.brand.has(name = field.brand))
        if field.gender:
            query = query.where(Watch.gender.has(name = field.gender))
        if field.case_material:
            query = query.where(Watch.case_material.has(name = field.case_material))
        if field.search_alias:
            search_words = field.search_alias.split()
            conditions = [
                Watch.alias.ilike(f"%{word}%") for word in search_words
            ]
            query = query.where(or_(*conditions)) 
            
    sort_column = getattr(Watch, field.sort_by, Watch.id)  
    query = query.order_by(sort_column)

    result = await session.execute(query)

    return [
        GetWatch(
            id=watch.id,
            folder=watch.folder,
            start_release=watch.start_release,
            end_release=watch.end_release,
            case_material=watch.case_material.name,
            gender=watch.gender,
            brand=watch.brand.name,
            alias = watch.alias.split()
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
            selectinload(Watch.user),
            selectinload(Watch.mechanism)
            .selectinload(Mechanism.mechanism_type)
        ).where(Watch.id == id)
    )
        
    watch = result.unique().scalar_one_or_none()

    if watch is None:
        return None

    return GetWatchId(
        id=watch.id,
        folder=watch.folder,
        code=watch.code,
        integrated_bracelet=watch.integrated_bracelet,
        start_release=watch.start_release,
        end_release=watch.end_release,
        gender=watch.gender,
        case_material=watch.case_material.name,
        factory=watch.factory.name,
        brand=watch.brand.name,
        updated = watch.updated,  
        alias = watch.alias.split(),
        mechanism_id = getattr(watch.mechanism, 'id', None),
        mechanism_code = getattr(watch.mechanism, 'code', None),
        mechanism_type= getattr(getattr(watch.mechanism, 'mechanism_type', None), 'name', None),
        user_name=watch.user.name,
        user_rating=watch.user.rating,
        user_avito=watch.user.avito,
        user_meshok=watch.user.meshok,
    )
