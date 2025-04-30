from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime

class GetWatch(BaseModel):
    id: int 
    folder: str
    start_release: int 
    end_release: int 
    gender: str 
    case_material: str 
    brand: str 
    alias: list[str]
    
class GetWatchId(BaseModel):
    id: int 
    folder: str
    code: int 
    description: str
    integrated_bracelet: bool 
    start_release: int 
    end_release: int 
    gender: str 
    case_material: str 
    mechanism: str 
    factory: str 
    brand: str 
    user: str 
    created_at: datetime 
    updated_at: datetime 
    alias: list[str]
    