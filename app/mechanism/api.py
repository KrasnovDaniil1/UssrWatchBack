from fastapi import APIRouter, Depends

from mechanism.schema import *
from mechanism.crud import *

from init.error import NotFoundError


router = APIRouter()

@router.get("/mechanisms")
async def get_mechanisms(field: GetMechanismField = Depends()) -> list[GetMechanism]:
    return await get_all_mechanism(field = field)

@router.get("/mechanisms/{id}")
async def get_mechanisms_id(id: int)-> GetMechanismId:
    mechanisms = await get_mechanism_by_id(id = id)
    
    if mechanisms is None:
        raise NotFoundError("Такого механизма нет в базе")
    return mechanisms 

# @router.put("/mechanisms/draft/{id}")
# def get_watch_id(id: int):
#     return  {"message": "Отправить механизм в черновик"}



