import uuid
from pydantic import BaseModel, Field


class PaymentMethodSchema(BaseModel):
    id: uuid.UUID
    name: str


class PaymentMethodRequest(BaseModel):
    name: str
