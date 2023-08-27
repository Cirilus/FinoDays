import http
from typing import List

import uuid
from fastapi import APIRouter, Depends
from loguru import logger
from starlette.responses import JSONResponse

from utils.errors import ErrEntityNotFound
from schemas.PaymentMethodSchema import PaymentMethodSchema, PaymentMethodRequest
from services.PaymentMethod import PaymentMethodServices
from convertors.PaymentMethod import PaymentMethodRequestToPaymentMethod
from utils.wrappers import error_wrapper

router = APIRouter(prefix="/api/v1/payment_method", tags=["payment_method"])


@router.get(
    "",
    response_model=List[PaymentMethodSchema],
    description="получение всех payment_method",
)
async def get_list(
        payment_service: PaymentMethodServices = Depends()
):
    logger.debug("payment_method - Route - get_list")
    payment_method = error_wrapper(payment_service.get_list)
    return payment_method


@router.get(
    "/{user_id}",
    response_model=PaymentMethodSchema,
    description="получение payment_method по uuid",
)
async def get_by_id(
        payment_method_id: uuid.UUID,
        payment_service: PaymentMethodServices = Depends()
):
    logger.debug("payment_method - Route - get_by_id")
    payment_method = error_wrapper(payment_service.get_by_id, payment_method_id)

    return payment_method


@router.patch(
    "/{user_id}",
    response_model=PaymentMethodSchema,
    description="обновление payment_method",
)
async def update(
        payment_method_id: uuid.UUID,
        payment_method_request: PaymentMethodRequest,
        payment_service: PaymentMethodServices = Depends()
):
    logger.debug("payment_method - Route - update")

    payment_method = PaymentMethodRequestToPaymentMethod(payment_method_request)

    payment_method = error_wrapper(payment_service.update, payment_method_id, payment_method)

    return payment_method


@router.delete(
    "/{user_id}",
    responses={200: {"msg": "successfully deleted"}},
    description="удаление payment_method",
)
async def delete(
        payment_method_id: uuid.UUID,
        payment_service: PaymentMethodServices = Depends()
):
    logger.debug("payment_method - Route - delete")
    response = error_wrapper(payment_service.delete, payment_method_id)
    if not response:
        response = JSONResponse(status_code=http.HTTPStatus.OK, content={"msg": "successfully deleted"})

    return response


@router.post(
    "",
    response_model=PaymentMethodSchema,
    description="создание payment_method",
)
async def create(
        payment_method_request: PaymentMethodRequest,
        payment_service: PaymentMethodServices = Depends()
):
    logger.debug("payment_method - Route - create")

    payment_method = PaymentMethodRequestToPaymentMethod(payment_method_request)

    payment_method = error_wrapper(payment_service.create, payment_method)

    return payment_method
