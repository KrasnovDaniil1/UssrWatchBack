from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import connection
from database.models import * 
from schemas.watch import GetWatch

@connection
async def get_all_watch(session: AsyncSession) -> list[GetWatch]:
    
    all_watch = (await session.execute(select(Watch))).scalars().all()
    
    for item in all_watch:
        item = item.to_dict()
        
    factory = (await session.execute(select(Factory))).scalars().all()
    brand = (await session.execute(select(Brand))).scalars().all()
    case_material = (await session.execute(select(CaseMaterial))).scalars().all()
    gender = (await session.execute(select(Gender))).scalars().all()
    function = (await session.execute(select(Function))).scalars().all()
    mechanism_type = (await session.execute(select(MechanismType))).scalars().all()
    
    return GetSeedData(
        factory_seed = [SeedItem(**item.to_dict()) for item in factory],
        brand_seed = [SeedItem(**item.to_dict()) for item in brand],
        case_material_seed = [SeedItem(**item.to_dict()) for item in case_material],
        gender_seed = [SeedItem(**item.to_dict()) for item in gender],
        function_seed = [SeedItem(**item.to_dict()) for item in function],
        mechanism_type_seed = [SeedItem(**item.to_dict()) for item in mechanism_type],
    )