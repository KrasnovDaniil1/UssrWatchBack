from fastapi import APIRouter

router = APIRouter()

@router.get("/mechanisms")
def read_root():
    return  {"message": 'sdf'}

@router.get("/mechanisms/{id}")
def read_root(id: int):
    return  {"message": "Подробно о механизме"}