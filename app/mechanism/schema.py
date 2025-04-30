from pydantic import BaseModel
from datetime import datetime

class GetMechanism(BaseModel):
    id: int 
    folder: str
    code: str
    release: int 
    mechanism_type: str 
    factory: str 
    
class GetMechanismId(BaseModel):
    id: int 
    folder: str 
    stones: int
    release: int
    description: str | None
    code: str 
    mechanism_type: str
    factory: str
    user: str
    function_all: list[str]
    created_at: datetime 
    updated_at: datetime 
    
    
    