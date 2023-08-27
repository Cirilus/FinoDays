from typing import List

from fastapi import Depends
from loguru import logger

from repositories.CFA import CFARepository
from models.cfa import CFA


class CFAService:
    def __init__(self, cfa_repo: CFARepository = Depends()) -> None:
        self.cfa_repo = cfa_repo

    def get_cfas(
            self, limit: int, offset: int, moderated: bool, payment_method: str
    ) -> List[CFA]:
        logger.debug("CFA - Service - get_cfas")
        result = self.cfa_repo.get_cfas(limit, offset,moderated,payment_method)
        return result
