from pydantic import BaseModel, EmailStr, SecretStr, Field

class UpdateSeedData(BaseModel):
    email: EmailStr = Field(..., min_length=3, max_length=50, description="Почта админа")
    token: SecretStr= Field(..., min_length=3, max_length=50, description="Токен админа")