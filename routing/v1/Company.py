from typing import List

from fastapi import APIRouter, Depends

from schemas.Company import Company
from services.Company import CompanyService

router = APIRouter(prefix="/api/v1/company", tags=["company"])


@router.get(
    "",
    response_model=List[Company],
    description="получение всех company",
)
async def get_all_cfa(company_service: CompanyService = Depends()):
    company = company_service.get_companies()
    return company
