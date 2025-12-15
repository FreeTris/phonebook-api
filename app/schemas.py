from pydantic import BaseModel
from typing import Optional


# -------- Users --------

class UserCreate(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


# -------- Contacts --------

class ContactCreate(BaseModel):
    name: str
    phone_number: str
    address: Optional[str] = None


class ContactOut(BaseModel):
    id: int
    name: str
    phone_number: str
    address: Optional[str]

    class Config:
        from_attributes = True
