from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from fastapi import Query

from typing import Optional


from database import connection
from database.models import * 
from schemas.mechanism import *

# не работает
@connection
async def get_all_mechanism(
    session: AsyncSession,
    mechanism_type: str = Query(None),
    search_code: Optional[str] = Query(None),
    sort_by: Optional[str] = Query("id")  
    ) -> list[GetMechanism]:
    
    query = select(Mechanism).options(
            selectinload(Mechanism.mechanism_type),
            selectinload(Mechanism.factory),
            selectinload(Mechanism.function_all).selectinload(MechanismFunction.function),
            
        ).order_by(Mechanism.id)
    
    if search_code:
        query = query.where(Mechanism.code == search_code)
    else:
        if mechanism_type:
            query = query.where(Mechanism.mechanism_type.has(name = mechanism_type))
            
    sort_column = getattr(Mechanism, sort_by, Mechanism.id)  
    query = query.order_by(sort_column)

    result = await session.execute(query)

    return [
        GetMechanism(
            id=mechanism.id,
            folder=mechanism.folder,
            release=mechanism.release,
            mechanism_type=mechanism.mechanism_type.name,
            code=mechanism.code,
            factory=mechanism.factory.name,
            function=[mf.function.name for mf in mechanism.function_all] 
        ) 
        for mechanism in result.unique().scalars().all()
    ]
    
@connection
async def get_mechanism_by_id(session: AsyncSession, id: int) -> GetMechanismId | None:
    
    result = await session.execute(
        select(Mechanism)
        .options(
            selectinload(Mechanism.mechanism_type),
            selectinload(Mechanism.factory),
            selectinload(Mechanism.user),
            selectinload(Mechanism.function_all).selectinload(MechanismFunction.function),
            
        ).where(Mechanism.id == id)
    )
    
    mechanism = result.unique().scalar_one_or_none()
    if mechanism is None:
        return None

    return GetMechanismId(
            id=mechanism.id,
            folder=mechanism.folder,
            stones=mechanism.stones,
            description=mechanism.description,
            
            user=mechanism.user.name,
            release=mechanism.release,
            mechanism_type=mechanism.mechanism_type.name,
            code=mechanism.code,
            factory=mechanism.factory.name,
            function_all=[mf.function.name for mf in mechanism.function_all],
            created_at = mechanism.created_at, 
            updated_at = mechanism.updated_at,  
        ) 

    