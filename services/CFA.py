from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from repositories.CFA import CFARepository
from models.cfa import CFA


class CFAService:
    def __init__(self, cfa_repo: CFARepository = Depends()) -> None:
        self.cfa_repo = cfa_repo

    def get_list(
            self, limit: int, offset: int, moderated: bool, payment_method: str
    ) -> List[CFA]:
        logger.debug("CFA - Service - get")
        result = self.cfa_repo.get_list(limit, offset, moderated, payment_method)
        return result

    def get_by_id(self, id: uuid.UUID) -> CFA:
        logger.debug("CFA - Service - get_by_id")
        result = self.cfa_repo.get_by_id(id)
        return result

    def delete(self, id: uuid.UUID) -> None:
        logger.debug("CFA - Service - delete")

        cfa = self.cfa_repo.get_by_id(id)

        self.cfa_repo.delete(cfa)
        return None

    def update(self, id: uuid.UUID, cfa: CFA) -> CFA:
        logger.debug("CFA - Service - update")
        result = self.cfa_repo.update(id, cfa)
        return result

    def create(self, cfa: CFA) -> CFA:
        logger.debug("CFA - Service - create")
        result = self.cfa_repo.create(cfa)
        return result