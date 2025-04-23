from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from typing import Optional, List
from datetime import datetime

class GetWatch(BaseModel):
    id: int = Field(..., description="ID часов")
    titul_src: HttpUrl = Field(..., description="Ссылка на главное изображение")
    code: int = Field(..., description="Номер оформления")
    integrated_bracelet: bool = Field(..., description="Есть ли браслет")
    start_release: int = Field(..., description="Начало производства")
    end_release: int = Field(..., description="Конец производства")
    gender: str = Field(..., description="Пол")
    case_material: str = Field(..., description="Материал корпуса")
    mechanism: str = Field(..., description="Механизм")
    factory: str = Field(..., description="Завод часов")
    brand: str = Field(..., description="Брэнд часов")
    user: str = Field(..., description="id пользователя часов")
    created_at: datetime = Field(..., description="Дата создание")
    update_at: datetime = Field(..., description="Дата обновления")
    
    
class GetWatchId(BaseModel):
    id: int = Field(..., description="ID часов")
    folder_src: list[HttpUrl] = Field(..., description="Список ссылок на изображения")
    code: int = Field(..., description="Номер оформления")
    integrated_bracelet: bool = Field(..., description="Есть ли браслет")
    start_release: int = Field(..., description="Начало производства")
    end_release: int = Field(..., description="Конец производства")
    gender: str = Field(..., description="Пол")
    case_material: str = Field(..., description="Материал корпуса")
    mechanism: str = Field(..., description="Механизм")
    factory: str = Field(..., description="Завод часов")
    brand: str = Field(..., description="Брэнд часов")
    user: str = Field(..., description="id пользователя часов")
    created_at: datetime = Field(..., description="Дата создание")
    update_at: datetime = Field(..., description="Дата обновления")
    
    
    

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