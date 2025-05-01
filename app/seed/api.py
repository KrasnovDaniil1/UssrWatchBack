from fastapi import APIRouter, Depends

from seed.schema import *
from seed.crud import *

from init.crud import *
from init.error import *


router = APIRouter()

@router.get("/seed")
async def get_seed() -> GetSeedData:
    return await get_seed_data()

@router.put("/seed")
async def put_seed(field: QueryAdmin = Depends()):
    if await update_seed_data(field = field):
        return {"message": "Данные обновлены"}

    raise NotFoundError("Отказано в доступе")