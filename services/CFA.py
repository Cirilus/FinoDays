from datetime import datetime
from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from models.History import History
from repositories.CFA import CFARepository
from models.cfa import CFA
from services.History import HistoryService


class CFAService:
    def __init__(self,
                 cfa_repo: CFARepository = Depends(),
                 history_repo: HistoryService = Depends()) -> None:
        self.cfa_repo = cfa_repo
        self.history_service = history_repo

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

        before_cfa = self.get_by_id(id)
        before_user_id = str(before_cfa.user_id)

        result = self.cfa_repo.update(id, cfa)

        if result.user_id != before_user_id:
            history = History(
                id=uuid.uuid4(),
                seller=before_user_id,
                recipient=cfa.user_id,
                cfa=cfa.id,
                count=cfa.count,
                price=cfa.price,
                created_at=datetime.utcnow(),
            )

            self.history_service.create(history)

        return result

    def create(self, cfa: CFA) -> CFA:
        logger.debug("CFA - Service - create")

        id = uuid.uuid4()
        cfa.id = id

        history = History(
            id=uuid.uuid4(),
            seller=None,
            recipient=cfa.user_id,
            cfa=cfa.id,
            count=cfa.count,
            price=cfa.price,
            created_at=datetime.utcnow(),
        )

        result = self.cfa_repo.create(cfa)

        self.history_service.create(history)
        return result
