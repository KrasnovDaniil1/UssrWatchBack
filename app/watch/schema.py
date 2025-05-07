from pydantic import BaseModel
from datetime import datetime
from typing import Literal, List

from database import seed_data as seed

class GetWatchField(BaseModel):
    search_aliases: str | None = None
    search_code: str | None = None
    brand: List[Literal[*seed.brand]] | None = None
    mechanism_type: List[Literal[*seed.mechanism_type]] | None = None
    case_material: List[Literal[*seed.case_material]] | None = None
    gender: List[Literal[*seed.gender]] | None = None 

class GetWatch(BaseModel):
    id: int 
    folder: str
    start_release: int | None = None
    end_release: int | None = None
    gender:  str | None = None 
    case_material: str | None = None  
    brand: str | None = None
    mechanism: str | None = None
    aliases: List[str] | None = None
    
class GetWatchId(BaseModel):
    id: int 
    folder: str
    description: str | None = None 
    start_release: int | None = None
    end_release: int | None = None
    gender:  str | None = None 
    case_material: str | None = None  
    brand: str | None = None
    mechanism: str | None = None
    mechanism_type: str | None = None
    code: int | None = None
    width_bracelet: int | None = None
    integrated_bracelet: bool 
    factory: str | None = None 
    aliases: List[str] | None = None
    functions: List[str] | None = None
    updated: datetime 

    