import http
from typing import List, Optional

import uuid
from fastapi import APIRouter, Depends
from loguru import logger
from starlette.responses import JSONResponse

from utils.errors import ErrEntityNotFound
from schemas.History import HistoryRequest, HistorySchema, HistoryResponse
from services.History import HistoryService
from convertors.History import HistoryRequestToHistory
from utils.wrappers import error_wrapper

router = APIRouter(prefix="/api/v1/history", tags=["history"])


@router.get(
    "",
    response_model=List[HistoryResponse],
    description="получение всех History",
)
async def get_list(
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        moderated: Optional[bool] = None,
        payment_method: Optional[str] = None,
        history_service: HistoryService = Depends()
):
    logger.debug("History - Route - get_list")
    history = error_wrapper(history_service.get_list,
                            limit, offset, moderated, payment_method
                            )
    return history


@router.get(
    "/{history_id}",
    response_model=HistorySchema,
    description="получение History по uuid",
)
async def get_by_id(
        history_id: uuid.UUID,
        history_service: HistoryService = Depends()
):
    logger.debug("History - Route - get_by_id")
    history = error_wrapper(history_service.get_by_id, history_id)
    return history


@router.post(
    "",
    response_model=HistorySchema,
    description="создание History",
)
async def create(
        history_request: HistoryRequest,
        history_service: HistoryService = Depends()
):
    logger.debug("History - Route - create")

    history = HistoryRequestToHistory(history_request)

    error_wrapper(history_service.create, history)

    return history
