from typing import List

from fastapi import Depends

from repositories.CFA import CFARepository
from models.cfa import CFA


class CFAService:
    def __init__(self, cfa_repo: CFARepository = Depends()) -> None:
        self.cfa_repo = cfa_repo

    def get_cfas(self) -> List[CFA]:
        result = self.cfa_repo.get_cfas()
        return result
