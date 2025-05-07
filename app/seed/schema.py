from pydantic import BaseModel

class IdName(BaseModel):
    id: int
    name: str

class TitleItems(BaseModel):
    title: str  
    items: list[IdName]
    
class GetSeedData(BaseModel):
    all_count_watch: int
    factory: TitleItems
    brand: TitleItems
    case_material: TitleItems
    function: TitleItems
    mechanism_type: TitleItems
    gender: TitleItems
    