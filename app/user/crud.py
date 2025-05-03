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

# @connection
# async def user_register(field: Register, session: AsyncSession) -> str | None:

@connection
async def user_authorization(field: FieldAuthorization, session: AsyncSession) -> UserAuthorization:
    result = await session.execute(
        select(User).where(User.email == field.email and User.provider_id == field.provider_id)
    )
        
    user = result.unique().scalar_one_or_none()
    if user is None:
        return None

    return GetUserId.model_validate(user, from_attributes=True)

