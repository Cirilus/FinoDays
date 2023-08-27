from typing import List, Optional

from fastapi import APIRouter, Depends
from loguru import logger

from schemas.cfa import CFA
from services.CFA import CFAService

router = APIRouter(prefix="/api/v1/cfa", tags=["cfa"])


@router.get(
    "",
    response_model=List[CFA],
    description="получение всех CFA",
)
async def get_all_cfa(
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        moderated: Optional[bool] = None,
        payment_method: Optional[str] = None,
        cfa_service: CFAService = Depends()
):
    logger.debug("CFA - Route - get_cfas")
    cfa = cfa_service.get_cfas(
        limit, offset,moderated,payment_method
    )
    return cfa

