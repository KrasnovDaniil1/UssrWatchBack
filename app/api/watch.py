from fastapi import APIRouter
from schemas.watch import GetWatch, GetWatchId
from crud.watch import get_all_watch

router = APIRouter()

@router.get("/watch")
async def get_watch() -> list[GetWatch]:
    return await get_all_watch()
    
@router.get("/watch/{id}")
def get_watch_id(id: int) -> GetWatchId:
    return  {"message": "Подробно о часах"}

@router.put("/watch/draft/{id}")
def get_watch_id(id: int):
    return  {"message": "Отправить часы в черновик"}

    