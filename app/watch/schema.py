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
    integrated_bracelet: bool 
    start_release: int | None = None
    end_release: int | None = None
    gender: str | None = None
    case_material: str 
    factory: str 
    brand: str 
    updated: datetime 
    alias: list[str] | None = None
    mechanism_id: int | None = None
    mechanism_code: str | None = None
    mechanism_code: str | None = None
    mechanism_type: str | None = None
    # function_all: list[str] | None = None
    user_name: str
    user_rating: int 
    user_avito: str | None = None
    user_meshok:str | None = None
    