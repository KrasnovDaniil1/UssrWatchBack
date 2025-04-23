from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from typing import Optional, List
from datetime import datetime

class GetMechanism(BaseModel):
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
    
class GetMechanismId(BaseModel):
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