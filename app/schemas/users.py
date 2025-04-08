from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    bio: str | None = Field(max_length=500)