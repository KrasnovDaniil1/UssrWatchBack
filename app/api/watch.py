from fastapi import APIRouter

router = APIRouter()

from app.schemas import watch 

@router.get("/watch")
def get_watch() -> list[watch.WatchSchema]:
    return  {"message": 'sdf'}
    
@router.get("/watch/{id}")
def get_watch_id(id: int):
    return  {"message": "Подробно о часах"}

@router.post("/watch")
def add_watch(watch: watch.WatchSchema):
    return  {"message": "Добавить часы"}

@router.put("/watch")
def add_watch():
    return  {"message": "Изменить часы"}

@router.delete("/watch")
def add_watch():
    return  {"message": "Удалить часы"}
    