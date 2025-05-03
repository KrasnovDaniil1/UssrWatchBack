from pydantic import BaseModel, EmailStr
from datetime import datetime

class FieldRegister(BaseModel):
    email: EmailStr

class FieldAuthorization(BaseModel):
    email: EmailStr
    provider_id: str

class UserAuthorization(BaseModel):
    id: int 
    name: str 
    rating: int 
    active: bool
    provider_id: str
    updated_at: datetime 
    avito: str | None
    meshok: str | None

class GetUserId(BaseModel):
    id: int 
    name: str 
    rating: int 
    active: bool
    updated_at: datetime 
    avito: str | None
    meshok: str | None



