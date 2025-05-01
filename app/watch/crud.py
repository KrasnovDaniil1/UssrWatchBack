from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload

from database import connection
from database.model import * 

from watch.schema import GetWatch, GetWatchId

from typing import Optional

@connection
async def get_watch_all(
    session: AsyncSession,          
    brand: Optional[str] = None,
    gender: Optional[str] = None,
    case_material: Optional[str] = None,
    search_alias: Optional[str] = None,
    search_code: Optional[str] = None,
    sort_by: str = "id"
    ) -> list[GetWatch]:
    
    query = select(Watch).options(
        selectinload(Watch.case_material),
        selectinload(Watch.brand),
        selectinload(Watch.mechanism),
        selectinload(Watch.user),
    )
    
    if search_code:
        query = query.where(Watch.code == search_code)
    else:
        if brand:
            query = query.where(Watch.brand.has(name=brand))
        if gender:
            query = query.where(Watch.gender.has(name=gender))
        if case_material:
            query = query.where(Watch.case_material.has(name=case_material))
        if search_alias:
            search_words = search_alias.split()
            conditions = [
                Watch.alias.ilike(f"%{word}%") for word in search_words
            ]
            query = query.where(or_(*conditions)) 
            
    sort_column = getattr(Watch, sort_by, Watch.id)  
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
            selectinload(Watch.mechanism),
            selectinload(Watch.user),
            
        ).where(Watch.id == id)
    )
        
    watch = result.unique().scalar_one_or_none()

    if watch is None:
        return None

    return GetWatchId(
        id=watch.id,
        folder=watch.folder,
        code=watch.code,
        description=watch.description,
        integrated_bracelet=watch.integrated_bracelet,
        start_release=watch.start_release,
        end_release=watch.end_release,
        created_at = watch.created_at, 
        updated_at = watch.updated_at,  
        factory=watch.factory.name,
        gender=watch.gender,
        case_material=watch.case_material.name,
        user=watch.user.name,
        brand=watch.brand.name,
        mechanism=watch.mechanism.code,
        alias = watch.alias.split()
    )
