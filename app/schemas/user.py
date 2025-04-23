from pydantic import BaseModel, EmailStr, SecretStr, Field, HttpUrl
from typing import Optional
from datetime import datetime

class GetUser(BaseModel):
    id: int = Field(..., description="ID пользователя")
    email: EmailStr = Field(..., description="Email пользователя")
    role: str = Field(..., description="Роль пользователя")
    rating: int = Field(..., description="Рэйтинг")
    created_at: datetime = Field(..., description="Дата создание")
    update_at: datetime = Field(..., description="Дата обновления")

class GetUserId(BaseModel):
    id: int = Field(..., description="ID пользователя")
    login: str = Field(..., description="Логин пользователя")
    password: SecretStr = Field(..., description="Пароль пользователя")
    email: EmailStr = Field(..., description="Email пользователя")
    role: str = Field(..., description="Роль пользователя")
    avito_url: HttpUrl = Field(..., description="Ссылка на авито")
    meshok_url: HttpUrl = Field(..., description="Ссылка на мешок")
    rating: int = Field(..., description="Рэйтинг")
    created_at: datetime = Field(..., description="Дата создание")
    update_at: datetime = Field(..., description="Дата обновления")

# нейронка
class UserBase(BaseModel):
    login: str = Field(..., min_length=3, max_length=50, description="Уникальный логин пользователя")
    email: EmailStr = Field(..., description="Уникальный email пользователя")

class UserAdd(UserBase):
    password: SecretStr = Field(..., min_length=8, description="Пароль (минимум 8 символов)")
    role_id: str = Field(..., description="ID роли пользователя")
    avito_url: Optional[str] = Field(None, max_length=255)
    meshok_url: Optional[str] = Field(None, max_length=255)

class UserPut(BaseModel):
    login: Optional[str] = Field(
        None, 
        min_length=3, 
        max_length=50, 
        description="Новый логин пользователя (уникальный)"
    )
    password: Optional[SecretStr] = Field(
        None,
        min_length=8,
        description="Новый пароль (минимум 8 символов)"
    )
    email: Optional[EmailStr] = Field(
        None, 
        description="Новый email пользователя (уникальный)"
    )
    role_id: Optional[str] = Field(
        None, 
        description="ID новой роли пользователя"
    )
    avito_url: Optional[str] = Field(
        None, 
        max_length=255, 
        description="Новая ссылка на профиль Avito"
    )
    meshok_url: Optional[str] = Field(
        None, 
        max_length=255, 
        description="Новая ссылка на профиль Meshok"
    )
