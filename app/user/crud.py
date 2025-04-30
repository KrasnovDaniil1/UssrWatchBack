from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload

from database import connection
from database.models import * 

from user.schema import GetUserId


@connection
async def get_user_by_id(id: int, session: AsyncSession) -> GetUserId | None:
    
    result = await session.execute(
        select(User).where(User.id == id)
    )
        
    user = result.unique().scalar_one_or_none()

    if user is None:
        return None

    return GetUserId(
        id = user.id,
        folder = user.folder,
        description = user.description,
        avito_url = user.avito_url,
        meshok_url = user.meshok_url,
        rating = user.rating,
        created_at = user.created_at,
    )
