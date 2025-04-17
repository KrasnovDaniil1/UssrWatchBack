from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def read_root():
    return  {"message": 'user'}
