import uuid
from datetime import datetime

from pydantic import BaseModel

from schemas.Company import Company
from schemas.UserSchema import UserResponse, UserRequest
from schemas.PaymentMethodSchema import PaymentMethodSchema


class CFASchema(BaseModel):
    id: uuid.UUID
    user: UserRequest
    company: Company
    count: int
    approved: bool
    price: float
    date_release: datetime
    payment_method: PaymentMethodSchema
    subject: str
    moderated: bool
    token: str


class CFAResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    company_id: uuid.UUID
    count: int
    approved: bool
    price: float
    date_release: datetime
    payment_method: uuid.UUID
    subject: str
    moderated: bool
    token: str


class CFARequest(BaseModel):
    user_id: uuid.UUID
    company_id: uuid.UUID
    count: int
    approved: bool
    price: float
    date_release: datetime
    payment_method: uuid.UUID
    subject: str
    moderated: bool
    token: str
