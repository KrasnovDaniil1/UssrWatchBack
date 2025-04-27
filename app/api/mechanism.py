from fastapi import APIRouter
from schemas.mechanism import GetMechanismId, GetMechanism

from crud.mechanism import get_all_mechanism

router = APIRouter()

@router.get("/mechanisms")
async def get_mechanisms() -> list[GetMechanism]:
    return await get_all_mechanism()

@router.get("/mechanisms/{id}")
def get_mechanisms_id(id: int)-> GetMechanismId:
    return  {"message": "получение конкретного механизма"}

@router.put("/mechanisms/draft/{id}")
def get_watch_id(id: int):
    return  {"message": "Отправить механизм в черновик"}



