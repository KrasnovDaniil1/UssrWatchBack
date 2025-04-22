from fastapi import APIRouter

router = APIRouter()

from schemas import users

@router.get("/user/{id}")
def get_user_id(id: int):
    return {"message": "Подробно о пользователе"}

@router.post("/user")
def add_user(user: users.UserAdd):
    return  {"message": "Добавить пользователя"}

@router.put("/user")
def change_user(user: users.UserPut):
    return  {"message": "Изменить пользователя"}

@router.delete("/user")
def remove_user(id: int):
    return  {"message": "Удалить пользователя"}

