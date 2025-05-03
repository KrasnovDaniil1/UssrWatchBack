from fastapi import APIRouter

from user.schema import *
from user.crud import *

from init.error import NotFoundError


router = APIRouter()

# @router.get("/user")
# def get_users_id() -> list[GetUser]:
#     return {"message": "Подробно о пользователе"}

@router.get("/user/{id}")
async def get_users_id(id: int) -> GetUserId:
    user = await get_user_by_id(id = id)

    if user is None:
        raise NotFoundError("Такого пользователя нет в базе")
    return user 

@router.post("/user/authorization")
def post_user_authorization(field: FieldAuthorization):
    user = user_authorization(field = field)
    if user is None:
        raise NotFoundError("Отказано в доступе")
    return user 



# @router.put("/user")
# def put_users_id():
#     return  {"message": "Изменить пользователя"}

# @router.delete("/user")
# def delete_users_id():
#     return  {"message": "добавление в черный список"}

