from pydantic import BaseModel


class PaymentMethod(BaseModel):
    id: str
    name: str
