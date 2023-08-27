from typing import List

from fastapi import APIRouter, Depends

from services.Company import CompanyService

router = APIRouter(prefix="/api/v1/company", tags=["company"])


@router.get(
    "",
    description="получение всех company",
)
async def get_all_cfa(company_service: CompanyService = Depends()):
    company = company_service.get_companies()
    return company
