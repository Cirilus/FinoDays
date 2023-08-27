from typing import List

from repositories.CFA import CFARepository
from schemas.cfa import CFA


class CFAService:
    def __init__(self, repo: CFARepository) -> None:
        self.repo = repo

    def get_cfas(self) -> List[CFA]:
        result = self.repo.get_CFAs()
        return result
