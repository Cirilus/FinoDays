import uuid

from pydantic import BaseModel

from schemas.Company import Company


class User(BaseModel):
    id: str
    company: Company
    name: str
    surname: str
    middelname: str
    location: str
    registry: str
    beneficial_owner: str

