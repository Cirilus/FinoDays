from typing import List

from fastapi import APIRouter, Depends

from schemas.cfa import CFA
from services.CFA import CFAService

router = APIRouter(prefix="/api/v1/cfa", tags=["cfa"])


@router.get(
    "",
    response_model=List[CFA],
    description="получение всех CFA",
)
async def get_all_cfa(cfa_service: CFAService = Depends()):
    cfa = cfa_service.get_cfas()
    return cfa

