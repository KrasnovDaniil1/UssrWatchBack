from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import connection
from database.models import Factory, Brand, CaseMaterial, Gender, Function, MechanismType, Role
from schemas.seed_data import GetSeedData, SeedItem

@connection
async def get_seed_data(session: AsyncSession) -> GetSeedData:
    factory = (await session.execute(select(Factory))).scalars().all()
    brand = (await session.execute(select(Brand))).scalars().all()
    case_material = (await session.execute(select(CaseMaterial))).scalars().all()
    gender = (await session.execute(select(Gender))).scalars().all()
    function = (await session.execute(select(Function))).scalars().all()
    mechanism_type = (await session.execute(select(MechanismType))).scalars().all()
    role = (await session.execute(select(Role))).scalars().all()

    return GetSeedData(
        factory_seed = [SeedItem(**item.to_dict()) for item in factory],
        brand_seed = [SeedItem(**item.to_dict()) for item in brand],
        case_material_seed = [SeedItem(**item.to_dict()) for item in case_material],
        gender_seed = [SeedItem(**item.to_dict()) for item in gender],
        function_seed = [SeedItem(**item.to_dict()) for item in function],
        mechanism_type_seed = [SeedItem(**item.to_dict()) for item in mechanism_type],
        role_seed = [SeedItem(**item.to_dict()) for item in role]
    )



# @connection
# async def update_brand(name:str, new_name: str, session: AsyncSession) -> int:
#     brand = Brand(name=name)
#     session.add(brand)
#     await session.commit()
#     return brand.id
