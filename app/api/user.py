from fastapi import APIRouter
from schemas.user import GetUserId, GetUser

router = APIRouter()

@router.post("/users/authorization")
def post_users_id():
    return  {"message": "Авторизация"}

@router.get("/users")
def get_users_id() -> list[GetUser]:
    return {"message": "Подробно о пользователе"}

@router.get("/users/{id}")
def get_users_id(id: int) -> GetUserId:
    return {"message": "Подробно о пользователе"}

@router.post("/users/{id}")
def post_users_id(id: int):
    return  {"message": "Добавить пользователя"}

@router.put("/users/{id}")
def put_users_id(id: int):
    return  {"message": "Изменить пользователя"}

@router.delete("/users/{id}")
def delete_users_id(id: int):
    return  {"message": "Удалить пользователя"}

