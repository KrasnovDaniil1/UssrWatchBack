from fastapi import APIRouter

router = APIRouter()

@router.post("/draft/watch")
def post_mechanisms_id():
    return  {"message": "Добавить часы в черновике"}

@router.put("/draft/watch")
def post_mechanisms_id():
    return  {"message": "изменить часы в черновике"}

@router.delete("/draft/watch")
def post_mechanisms_id():
    return  {"message": "удалить из черновика часы"}

@router.post("/draft/watch/main")
def post_mechanisms_id():
    return  {"message": "Отправить часы в основную таблицу"}



@router.post("/draft/mechanism")
def post_mechanisms_id():
    return  {"message": "Добавить механизм в черновике"}

@router.put("/draft/mechanism")
def post_mechanisms_id():
    return  {"message": "изменить механизм в черновике"}

@router.delete("/draft/mechanism")
def post_mechanisms_id():
    return  {"message": "удалить из черновика механизм"}

@router.post("/draft/mechanism/main")
def post_mechanisms_id():
    return  {"message": "Отправить механизм в основную таблицу"}


