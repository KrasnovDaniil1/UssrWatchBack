from pydantic import BaseModel, EmailStr, SecretStr

class IdName(BaseModel):
    id: int | str  
    name: str
class GetSeedData(BaseModel):
    all_count_watch: int
    factory: list[IdName]
    brand: list[IdName]
    case_material: list[IdName]
    function: list[IdName]
    mechanism_type: list[IdName]
    gender: list[IdName]
    