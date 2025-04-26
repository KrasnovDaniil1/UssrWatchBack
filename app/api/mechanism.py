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

@router.post("/mechanisms/{id}")
def post_mechanisms_id(id: int):
    return  {"message": "Добавить механизма"}

@router.put("/mechanisms/{id}")
def put_mechanisms_id(id: int):
    return  {"message": "Изменить механизма"}

@router.delete("/mechanisms/{id}")
def delete_mechanisms_id(id: int):
    return  {"message": "Удалить механизма"}

