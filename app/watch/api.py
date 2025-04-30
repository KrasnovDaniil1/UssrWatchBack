from fastapi import APIRouter, Query
from watch.schema import GetWatch, GetWatchId
from watch.crud import get_watch_all, get_watch_by_id

from init.error import NotFoundError

from typing import Optional

router = APIRouter()

@router.get("/watch")
async def get_watch(
    brand: Optional[str] = Query(None),
    gender: Optional[str] = Query(None),
    case_material: Optional[str] = Query(None),
    search_alias: Optional[str] = Query(None),
    search_code: Optional[str] = Query(None),
    sort_by: Optional[str] = Query("id")  
    ) -> list[GetWatch]:
    
    watch = await get_watch_all(
        brand=brand, 
        gender=gender, 
        case_material=case_material, 
        search_alias=search_alias,
        search_code=search_code,
        sort_by=sort_by
    )

    return watch 
    
@router.get("/watch/{id}")
async def get_watch_id(id: int) -> GetWatchId:
    watch = await get_watch_by_id(id)
    
    if watch is None:
        raise NotFoundError("Таких часов нет в базе")
    return watch 


@router.put("/watch/draft/{id}")
def get_watch_id(id: int):
    return  {"message": "Отправить часы в черновик"}

    