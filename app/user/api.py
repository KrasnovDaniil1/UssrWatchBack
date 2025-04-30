from fastapi import APIRouter

from user.schema import GetUserId, GetUser
from user.crud import get_user_by_id

from init.error import NotFoundError


router = APIRouter()

@router.post("/users/authorization")
def post_users_id():
    return  {"message": "Авторизация"}

@router.get("/users")
def get_users_id() -> list[GetUser]:
    return {"message": "Подробно о пользователе"}

@router.get("/users/{id}")
async def get_users_id(id: int) -> GetUserId:
    user = await get_user_by_id(id = id)
    
    if user is None:
        raise NotFoundError("Такого пользователя нет в базе")
    return user 

@router.put("/users/{id}")
def put_users_id(id: int):
    return  {"message": "Изменить пользователя"}

@router.delete("/users/{id}")
def delete_users_id(id: int):
    return  {"message": "добавление в черный список"}

