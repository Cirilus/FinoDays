import uuid

from pydantic import BaseModel

from schemas.Company import Company


class UserSchema(BaseModel):
    id: uuid.UUID
    login: str
    password_hashed: str
    company: Company
    name: str
    surname: str
    middelname: str
    location: str
    registry: str
    beneficial_owner: str
    
class UserRequest(BaseModel):
    login: str
    password_hashed: str
    company: Company
    name: str
    surname: str
    middelname: str
    location: str
    registry: str
    beneficial_owner: str

