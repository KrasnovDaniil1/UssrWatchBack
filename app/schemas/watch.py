from pydantic import BaseModel

class Watch(BaseModel):
    name: str
    material: list