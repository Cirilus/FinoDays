from datetime import datetime
from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from models.History import History
from repositories.History import HistoryRepository
from utils.errors import ErrEntityConflict


class HistoryService:
    def __init__(self, history_repo: HistoryRepository = Depends()) -> None:
        self.history_repo = history_repo

    def get_list(
            self, offset: int, limit: int,
            date: datetime | None, user: uuid.UUID | None,
            cfa: uuid.UUID | None
    ) -> List[History]:
        logger.debug("History - Service - get_list")
        result = self.history_repo.get_list(
            offset, limit, date, user, cfa
        )
        return result

    def get_by_id(self, id: uuid.UUID) -> History:
        logger.debug("History - Service - get_by_id")
        result = self.history_repo.get_by_id(id)
        return result

    def create(self, history: History) -> History:
        logger.debug("History - Service - create")

        if history.seller.id == history.recipient.id:
            raise ErrEntityConflict("the seller id should not be equal recipient id")

        result = self.history_repo.create(history)
        return result
