import uuid

from pydantic import BaseModel

from schemas.Company import Company


class UserSchema(BaseModel):
    id: uuid.UUID
    login: str
    company: Company
    name: str
    surname: str
    middelname: str
    location: str
    registry: str
    beneficial_owner: str


class UserResponse(BaseModel):
    id: uuid.UUID
    login: str
    password_hashed: str
    company: uuid.UUID
    name: str
    surname: str
    middelname: str
    location: str
    registry: str
    beneficial_owner: str


class TokenUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserRequest(BaseModel):
    company: uuid.UUID
    login: str
    name: str
    surname: str
    middelname: str
    location: str
    registry: str
    beneficial_owner: str