from fastapi import APIRouter

from schemas.seed_data import UpdateSeedData, GetSeedData

from crud.seed_data import get_seed_data

from crud import create_data

router = APIRouter()

@router.get("/seed_data")
async def get_user_id() -> GetSeedData:
    return await get_seed_data()

# добавить проверку для админа
@router.put("/update_seed_data")
async def get_user_id(auth_admin: UpdateSeedData):
    return await create_data()
