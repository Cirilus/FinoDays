import uuid

from pydantic import BaseModel


class Company(BaseModel):
    id: uuid.UUID
    name: str
