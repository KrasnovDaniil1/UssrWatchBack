from pydantic import BaseModel, ConfigDict

class WatchGet(BaseModel):
    name: str
    case_material: list[str] | None
    integrated_bracelet: bool | None
    mechanism: list[str] | None
    brand: list[str] | None
    gender: str | None
    update: str
    
    model_config = ConfigDict(extra="forbid")