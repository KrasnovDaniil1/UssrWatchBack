from pydantic import BaseModel
from datetime import datetime

class GetMechanismField(BaseModel):
    mechanism_type: str | None = None
    search_code: str | None = None
    sort_by: str = "id"

class GetMechanism(BaseModel):
    id: int 
    stones: int 
    folder: str
    code: str
    release: int 
    mechanism_type: str 
    factory: str 
    
class GetMechanismId(BaseModel):
    id: int 
    folder: str 
    stones: int
    release: int | None = None
    description: str | None = None
    code: str 
    mechanism_type: str
    factory: str
    user: str
    function_all: list[str]
    created: datetime 
    updated: datetime 
    
    
    