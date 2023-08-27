import uuid
from datetime import datetime

from pydantic import BaseModel

from schemas.Company import Company
from schemas.User import User
from schemas.PaymentMethod import PaymentMethod


class CFA(BaseModel):
    id: str
    user: User
    company: Company
    count: int
    approved: bool
    price: float
    date_release: datetime
    payment_method: PaymentMethod
    subject: str
    moderated: bool
    token: str
