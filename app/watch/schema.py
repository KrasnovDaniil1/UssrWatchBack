from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class GetWatchField(BaseModel):
    brand: str | None = None
    gender: str | None = None
    case_material: str | None = None
    search_alias: str | None = None
    search_code: str | None = None
    sort_by: str = "id"

class GetWatch(BaseModel):
    id: int 
    folder: str
    start_release: int | None = None
    end_release: int | None = None
    gender: str 
    case_material: str 
    brand: str 
    alias: list[str] | None = None
    
class GetWatchId(BaseModel):
    id: int 
    folder: str
    code: int | None = None
    description: str | None = None
    integrated_bracelet: bool 
    start_release: int | None = None
    end_release: int | None = None
    gender: str | None = None
    case_material: str 
    mechanism: str 
    factory: str 
    brand: str 
    user: str 
    created: datetime 
    updated: datetime 
    alias: list[str] | None = None
    