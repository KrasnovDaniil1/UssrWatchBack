from pydantic import BaseModel, EmailStr, SecretStr

class QueryAdmin(BaseModel):
    login_admin: str 
    password_admin: str

class UpdateSeedData(BaseModel):
    email: EmailStr 
    provider_id: SecretStr


class IdName(BaseModel):
    id: int | str  
    name: str
class GetSeedData(BaseModel):
    all_count_watch: int
    all_count_mechanism: int
    factory: list[IdName]
    brand: list[IdName]
    case_material: list[IdName]
    function: list[IdName]
    mechanism_type: list[IdName]
    gender: list[IdName]
    