import http
from typing import List, Optional

import uuid

from fastapi import APIRouter, Depends
from loguru import logger
from starlette.responses import JSONResponse

from utils.errors import ErrEntityNotFound
from schemas.CFA import CFARequest, CFASchema, CFAResponse
from services.CFA import CFAService
from convertors.CFA import CFARequestCreateToCFA, CFAToCFASchema
from utils.wrappers import error_wrapper

router = APIRouter(prefix="/api/v1/cfa", tags=["cfa"])


@router.get(
    "",
    response_model=List[CFASchema],
    description="получение всех CFA",
)
async def get_list(
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        moderated: Optional[bool] = None,
        payment_method: Optional[str] = None,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfas")
    cfa = error_wrapper(cfa_service.get_list,
                        limit, offset, moderated, payment_method
                        )
    if type(cfa) != JSONResponse:
        cfa = [CFAToCFASchema(c) for c in cfa]
    return cfa


@router.get(
    "/{cfa_id}",
    response_model=CFAResponse,
    description="получение CFA по uuid",
)
async def get_by_id(
        cfa_id: uuid.UUID,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")
    cfa = error_wrapper(cfa_service.get_by_id, cfa_id)
    return cfa


@router.patch(
    "/{cfa_id}",
    response_model=CFAResponse,
    description="обновление CFA",
)
async def update(
        cfa_id: uuid.UUID,
        cfa_request: CFARequest,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")

    cfa = CFARequestCreateToCFA(cfa_request)
    cfa = error_wrapper(cfa_service.update, cfa_id, cfa)
    return cfa


@router.delete(
    "/{cfa_id}",
    responses={200: {"msg": "successfully deleted"}},
    description="удаление CFA",
)
async def delete(
        cfa_id: uuid.UUID,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")
    response = error_wrapper(cfa_service.delete, cfa_id)
    if not response:
        response = JSONResponse(status_code=http.HTTPStatus.OK, content={"msg": "successfully deleted"})
    return response


@router.post(
    "",
    response_model=CFAResponse,
    description="создание CFA",
)
async def create(
        cfa_request: CFARequest,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")

    cfa = CFARequestCreateToCFA(cfa_request)
    cfa = error_wrapper(cfa_service.create, cfa)

    return cfa
