from models.PaymentMethod import PaymentMethod
from schemas.PaymentMethodSchema import PaymentMethodRequest


def PaymentMethodRequestToPaymentMethod(payment: PaymentMethodRequest) -> PaymentMethod:
    result = PaymentMethod()
    result.name = payment.name
    return result
