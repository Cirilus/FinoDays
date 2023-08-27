import http
from typing import List, Optional

import uuid
from fastapi import APIRouter, Depends
from loguru import logger
from starlette.responses import JSONResponse

from utils.errors import ErrEntityNotFound
from schemas.CFAchema import CFARequest, CFASchema
from services.CFA import CFAService
from convertors.CFA import CFARequestToCFA

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
    cfa = cfa_service.get_list(
        limit, offset, moderated, payment_method
    )
    return cfa


@router.get(
    "/{user_id}",
    response_model=CFASchema,
    description="получение CFA по uuid",
)
async def get_by_id(
        cfa_id: uuid.UUID,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")
    try:
        cfa = cfa_service.get_by_id(cfa_id)
    except ErrEntityNotFound as e:
        return JSONResponse(status_code=http.HTTPStatus.NOT_FOUND, content={"msg": str(e)})
    except Exception as e:
        logger.error(f"CFA - Route - get_cfa_by_id, err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, content={"msg": str(e)})
    return cfa


@router.patch(
    "/{user_id}",
    response_model=CFASchema,
    description="обновление CFA",
)
async def update(
        cfa_id: uuid.UUID,
        cfa_request: CFARequest,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")

    cfa = CFARequestToCFA(cfa_request)

    try:
        cfa = cfa_service.update(cfa_id, cfa)
    except Exception as e:
        logger.error(f"CFA - Route - get_cfa_by_id, err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, content={"msg": str(e)})
    return cfa


@router.delete(
    "/{user_id}",
    responses={200: {"msg": "successfully deleted"}},
    description="удаление CFA",
)
async def delete(
        cfa_id: uuid.UUID,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")
    try:
        cfa_service.delete(cfa_id)
    except ErrEntityNotFound as e:
        return JSONResponse(status_code=http.HTTPStatus.NOT_FOUND, content={"msg": str(e)})
    except Exception as e:
        logger.error(f"CFA - Route - get_cfa_by_id, err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, content={"msg": str(e)})
    return JSONResponse(status_code=http.HTTPStatus.OK, content={"msg": "successfully deleted"})


@router.post(
    "",
    response_model=CFASchema,
    description="создание CFA",
)
async def create(
        cfa_request: CFARequest,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfa_by_id")

    cfa = CFARequestToCFA(cfa_request)

    try:
        cfa = cfa_service.create(cfa)
    except Exception as e:
        logger.error(f"CFA - Route - get_cfa_by_id, err = {e}")
        return JSONResponse(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, content={"msg": str(e)})
    return cfa
