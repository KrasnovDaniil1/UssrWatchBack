from fastapi import APIRouter

from schemas.seed_data import UpdateSeedData, GetSeedData

from crud.seed_data import get_seed_data

from crud import create_data

router = APIRouter()

@router.get("/seed_data")
async def get_user_id() -> GetSeedData:
    try:
        return await get_seed_data()
    except:
        return {"error": "Данные не получены"}

# добавить проверку для админа
@router.put("/update_seed_data")
async def get_user_id(auth_admin: UpdateSeedData):
    try:
        return await create_data()
    except:
        return {"message": "Ошибка Обновление данных"}
