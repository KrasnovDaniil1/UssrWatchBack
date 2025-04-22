from fastapi import APIRouter

router = APIRouter()

from schemas import watch 

@router.get("/watch")
def get_watch() -> list[watch.WatchBase]:
    return  {"message": 'sdf'}
    
@router.get("/watch/{id}")
def get_watch_id(id: int):
    return  {"message": "Подробно о часах"}

@router.post("/watch")
def add_watch(watch: watch.WatchAdd):
    return  {"message": "Добавить часы"}

@router.put("/watch")
def add_watch(watch: watch.WatchPut):
    return  {"message": "Изменить часы"}

@router.delete("/watch")
def remove_watch(id: int):
    return  {"message": "Удалить часы"}
    