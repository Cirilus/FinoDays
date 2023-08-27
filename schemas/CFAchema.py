import uuid
from datetime import datetime

from pydantic import BaseModel

from schemas.Company import Company
from schemas.User import User
from schemas.PaymentMethodSchema import PaymentMethodSchema


class CFASchema(BaseModel):
    id: uuid.UUID
    user: User
    company: Company
    count: int
    approved: bool
    price: float
    date_release: datetime
    payment_method: PaymentMethodSchema
    subject: str
    moderated: bool
    token: str


class CFARequest(BaseModel):
    user: uuid.UUID
    company: uuid.UUID
    count: int
    approved: bool
    price: float
    date_release: datetime
    payment_method: uuid.UUID
    subject: str
    moderated: bool
    token: str
