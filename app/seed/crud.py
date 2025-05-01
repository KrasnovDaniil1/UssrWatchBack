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
    all_count_watch = await session.scalar(select(func.count()).select_from(Watch))
    all_count_mechanism = await session.scalar(select(func.count()).select_from(Mechanism))
    
    return GetSeedData(
        all_count_watch=all_count_watch,
        all_count_mechanism=all_count_mechanism,
        factory=[{"id": item.id, "name": item.name} for item in factory],
        brand=[{"id": item.id, "name": item.name} for item in brand],
        case_material=[{"id": item.id, "name": item.name} for item in case_material],
        function=[{"id": item.id, "name": item.name} for item in function],
        mechanism_type=[{"id": item.id, "name": item.name} for item in mechanism_type],
        gender=[
            {"id": "m", "name": "Мужские"},
            {"id": "w", "name": "Женские"},
            {"id": "a", "name": "Универсальные"}
        ]
    )

@connection
async def update_seed_data(
    session: AsyncSession,
    field: QueryAdmin
    ) -> bool:
    result = await session.execute(
        select(Admin).where(Admin.login == field.login_admin)
    )
    admin = result.scalar_one_or_none()

    if admin is None or admin.password != field.password_admin:
        return False
    return True
    
