from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from database import connection
from database.model import *

from seed.schema import *

@connection
async def get_seed_data(session: AsyncSession) -> GetSeedData:
    factory = (await session.execute(select(Factory))).scalars().all()
    brand = (await session.execute(select(Brand))).scalars().all()
    case_material = (await session.execute(select(CaseMaterial))).scalars().all()
    function = (await session.execute(select(Function))).scalars().all()
    mechanism_type = (await session.execute(select(MechanismType))).scalars().all()
    gender = (await session.execute(select(Gender))).scalars().all()
    all_count_watch = await session.scalar(select(func.count()).select_from(Watch))
    
    return GetSeedData(
        all_count_watch=all_count_watch,
        factory = {
            "title": "Часовые заводы",
            "items": [{"id": item.id, "name": item.name} for item in factory]
        },
        brand = {
            "title": "Марки",
            "items": [{"id": item.id, "name": item.name} for item in brand]
        },
        case_material = {
            "title": "Материал корпуса",
            "items": [{"id": item.id, "name": item.name} for item in case_material]
        },
        function = {
            "title": "Функции часов",
            "items": [{"id": item.id, "name": item.name} for item in function]
        },
        mechanism_type = {
            "title": "Тип механизма",
            "items": [{"id": item.id, "name": item.name} for item in mechanism_type]
        },
        gender = {
            "title": "Пол",
            "items": [{"id": item.id, "name": item.name} for item in gender]
        },
        
    )

# @connection
# async def update_seed_data(
#     session: AsyncSession,
#     field: QueryAdmin
#     ) -> bool:
#     # result = await session.execute(
#     #     select(Admin).where(Admin.login == field.login)
#     # )
#     admin = result.scalar_one_or_none()

#     if admin is None or admin.password != field.password:
#         return False
#     return True
    
