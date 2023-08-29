import uuid
from datetime import datetime

from pydantic import BaseModel

from schemas.CFASchema import CFASchema
from schemas.UserSchema import UserSchema


class HistorySchema(BaseModel):
    id: uuid.UUID
    seller: UserSchema
    recipient: UserSchema
    cfa: CFASchema
    count: int
    price: float
    created_at: datetime


class HistoryResponse(BaseModel):
    id: uuid.UUID
    seller: uuid.UUID | None = None
    recipient: uuid.UUID
    cfa: uuid.UUID
    count: int
    price: float


class HistoryRequest(BaseModel):
    seller: uuid.UUID | None = None
    recipient: uuid.UUID
    cfa: uuid.UUID
    count: int
    price: float
