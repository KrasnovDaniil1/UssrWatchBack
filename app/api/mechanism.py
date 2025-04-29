from fastapi import APIRouter, Query
from schemas.mechanism import GetMechanismId, GetMechanism

from crud.mechanism import get_all_mechanism, get_mechanism_by_id

from api.errors import NotFoundError

from typing import Optional

router = APIRouter()

@router.get("/mechanisms")
async def get_mechanisms(
    mechanism_type: str = Query(None),
    search_code: Optional[str] = Query(None),
    sort_by: Optional[str] = Query("id")  
    ) -> list[GetMechanism]:
    return await get_all_mechanism(
        mechanism_type = mechanism_type,
        search_code = search_code,
        sort_by = sort_by
    )

@router.get("/mechanisms/{id}")
async def get_mechanisms_id(id: int)-> GetMechanismId:
    mechanisms = await get_mechanism_by_id(id = id)
    
    if mechanisms is None:
        raise NotFoundError("Такого механизма нет в базе")
    return mechanisms 

@router.put("/mechanisms/draft/{id}")
def get_watch_id(id: int):
    return  {"message": "Отправить механизм в черновик"}



