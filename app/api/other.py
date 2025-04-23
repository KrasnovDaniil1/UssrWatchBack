from fastapi import APIRouter

from schemas.other import UpdateSeedData

router = APIRouter()

@router.get("/update_seed_data")
def get_user_id(body: UpdateSeedData):
    return {"message": "Обновление данных"}


