from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database import connection
from database.models import * 
from schemas.mechanism import GetMechanism

# не работает
@connection
async def get_all_mechanism(session: AsyncSession) -> list[GetMechanism]:
    
    result = await session.execute(
        select(Mechanism)
        .options(
            selectinload(Mechanism.mechanism_type),
            selectinload(Mechanism.factory),
            selectinload(Mechanism.function_all),
            
        )
        )
    all_mechanism = result.scalars().all()
    mechanisms = []

    for mechanism in all_mechanism:
        mechanisms.append(GetMechanism(
            id=mechanism.id,
            folder=mechanism.folder,
            release=mechanism.release,
            mechanism_type=mechanism.mechanism_type,
            factory=mechanism.factory,
            function=[function.name for function in mechanism.function_all]
            
        ))
    
    return mechanisms