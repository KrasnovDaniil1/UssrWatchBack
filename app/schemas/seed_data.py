from pydantic import BaseModel, EmailStr, SecretStr, Field

class UpdateSeedData(BaseModel):
    email: EmailStr = Field(..., description="Почта админа")
    token: SecretStr= Field(..., description="Токен админа")

class SeedItem(BaseModel):
    id: int
    name: str  

class GetSeedData(BaseModel):
    factory_seed: list[SeedItem]
    brand_seed: list[SeedItem]
    case_material_seed: list[SeedItem]
    gender_seed: list[SeedItem]
    function_seed: list[SeedItem]
    mechanism_type_seed: list[SeedItem]
    role_seed: list[SeedItem]
    