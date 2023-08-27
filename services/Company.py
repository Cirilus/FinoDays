from typing import List

from fastapi import Depends

from repositories.Company import CompanyRepository
from models.Company import Company


class CompanyService:
    def __init__(self, company_repo: CompanyRepository = Depends()) -> None:
        self.company_repo = company_repo

    def get_companies(self) -> List[Company]:
        companies = self.company_repo.get_companies()
        return companies
