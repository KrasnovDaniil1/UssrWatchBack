from pydantic import BaseModel, EmailStr
from datetime import datetime

class GetUserId(BaseModel):
    id: int 
    name: str 
    rating: int 
    active: bool
    email: EmailStr
    created_at: datetime 
    updated_at: datetime 
    avatar_url: str | None
    avito_url: str | None
    meshok_url: str | None



