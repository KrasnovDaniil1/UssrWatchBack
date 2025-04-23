from fastapi import APIRouter
from schemas.watch import GetWatch, GetWatchId

router = APIRouter()

@router.get("/watch")
def get_watch() -> list[GetWatch]:
    return  {"message": 'список часов'}
    
@router.get("/watch/{id}")
def get_watch_id(id: int) -> GetWatchId:
    return  {"message": "Подробно о часах"}

@router.post("/watch/{id}")
def post_watch_id(id: int):
    return  {"message": "Добавить часы"}

@router.put("/watch/{id}")
def put_watch_id(id: int):
    return  {"message": "Изменить часы"}

@router.delete("/watch/{id}")
def delete_watch_id(id: int):
    return  {"message": "Удалить часы"}
    