import uuid

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # user_id: uuid.UUID
    login: str | None = None
