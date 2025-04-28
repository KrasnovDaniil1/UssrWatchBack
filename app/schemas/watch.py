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
    

# нейронка
class WatchBase(BaseModel):
    name: str = Field(..., max_length=50, description="Название часов")
    code: str = Field(..., max_length=50, description="Уникальный номер оформления", unique=True)
    integrated_bracelet: bool = Field(default=False, description="Есть ли интегрированный браслет")

class WatchAdd(WatchBase):
    gender_id: int = Field(..., gt=0, description="ID пола")
    case_material_id: int = Field(..., gt=0, description="ID материала корпуса")
    mechanism_id: int = Field(..., gt=0, description="ID механизма")
    factory_id: int = Field(..., gt=0, description="ID завода-изготовителя")
    brand_id: int = Field(..., gt=0, description="ID бренда")
    user_id: int = Field(..., gt=0, description="ID пользователя")

class WatchPut(BaseModel):
    name: Optional[str] = Field(None, description="Новое название часов")
    integrated_bracelet: Optional[bool] = Field(
        None,
        description="Обновленное состояние браслета"
    )
    gender_id: Optional[int] = Field(
        None, gt=0,
        description="Новый ID пола"
    )
    case_material_id: Optional[int] = Field(
        None, gt=0,
        description="Новый ID материала корпуса"
    )
    mechanism_id: Optional[int] = Field(
        None, gt=0,
        description="Новый ID механизма"
    )
    factory_id: Optional[int] = Field(
        None, gt=0,
        description="Новый ID завода"
    )
    brand_id: Optional[int] = Field(
        None, gt=0,
        description="Новый ID бренда"
    )
    
    model_config = ConfigDict(extra="forbid")