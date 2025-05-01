from fastapi import APIRouter

from seed.schema import UpdateSeedData, GetSeedData
from seed.crud import get_seed_data

from init.crud import create_data

router = APIRouter()

@router.get("/seed")
async def get_user_id() -> GetSeedData:
    return await get_seed_data()

@router.put("/seed")
async def get_user_id(auth_admin: UpdateSeedData):
    return await create_data()
