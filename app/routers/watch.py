from fastapi import APIRouter

router = APIRouter()

@router.get("/watch")
def read_root():
    return  {"message": 'sdf'}

@router.get("/watch/{id}")
def read_root(id: int):
    return  {"message": "Подробно о часах"}