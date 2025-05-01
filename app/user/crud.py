from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import connection
from database.model import * 

from user.schema import *


@connection
async def get_user_by_id(id: int, session: AsyncSession) -> GetUserId | None:
    result = await session.execute(
        select(User).where(User.id == id)
    )
        
    user = result.unique().scalar_one_or_none()
    if user is None:
        return None

    return GetUserId.model_validate(user, from_attributes=True)

