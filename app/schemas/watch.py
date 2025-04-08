from pydantic import BaseModel, ConfigDict

class WatchSchema(BaseModel):
    name: str
    material: list[str] | None
    
    model_config = ConfigDict(extra="forbid")