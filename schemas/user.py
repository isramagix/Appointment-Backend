from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: str | None = None
    password: str | None = None


class UserOut(UserBase):
    id: int
    role: str
    created_at: datetime

    class Config:
        orm_mode = True
