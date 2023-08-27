from typing import List

import uuid
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

    def get_cfa_by_id(self, id: uuid.UUID) -> CFA:
        logger.debug("CFA - Service - get_cfa_by_id")
        result = self.cfa_repo.get_cfa_by_id(id)
        return result

    def delete_cfa(self, id: uuid.UUID) -> None:
        logger.debug("CFA - Service - delete_cfa")
        self.cfa_repo.delete_cfa(id)
        return None

    def update_cfa(self, id: uuid.UUID, cfa: CFA) -> CFA:
        logger.debug("CFA - Service - update_cfa")
        result = self.cfa_repo.update_cfa(id, cfa)
        return result