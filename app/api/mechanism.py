from fastapi import APIRouter
from schemas.mechanism import GetMechanismId, GetMechanism

router = APIRouter()

@router.get("/mechanisms")
def get_mechanisms() -> list[GetMechanism]:
    return  {"message": 'получение всех механизмов'}

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

