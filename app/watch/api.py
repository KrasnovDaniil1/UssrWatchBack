from fastapi import APIRouter, Depends

from watch.schema import *
from watch.crud import *

from init.error import NotFoundError


router = APIRouter()


@router.post("/watch")
async def get_watch(field: GetWatchField = Depends()) -> list[GetWatch]:
    watch = await get_watch_all(field = field)
    return watch 
    
    
@router.get("/watch/{id}")
async def get_watch_id(id: int) -> GetWatchId:
    watch = await get_watch_by_id(id)
    
    if watch is None:
        raise NotFoundError("Таких часов нет в базе")
    return watch 


# @router.put("/watch/draft/{id}")
# def get_watch_id(id: int):
#     return  {"message": "Отправить часы в черновик"}

    