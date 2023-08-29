import uuid
from datetime import datetime
from typing import List

from fastapi import Depends
from loguru import logger
from sqlalchemy import or_

from configs.Database import get_db_connection
from models.History import History
from sqlalchemy.orm import Session, lazyload
from utils.errors import ErrEntityNotFound


class HistoryRepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_list(
            self, offset: int, limit: int,
            date: datetime | None, user: uuid.UUID | None,
            cfa: uuid.UUID | None
    ) -> List[History]:
        logger.debug("History - Repository - get_list")
        query = self.db.query(History)
        if user:
            query = query.filter(or_(History.seller == user, History.recipient == user))
        if cfa:
            query = query.filter_by(cfa=cfa)
        if date:
            query = query.filter(History.created_at < date)
        history_list = query.offset(offset).limit(limit).all()
        return history_list

    def get_by_id(self, id: uuid.UUID) -> History:
        logger.debug("History - Repository - get_by_id")
        history = self.db.get(
            History,
            id
        )
        if history is None:
            raise ErrEntityNotFound("error entity not found")
        return history

    def create(self, history: History) -> History:
        logger.debug("History - Repository - create")
        id = uuid.uuid4()
        history.id = id
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)
        return history

    def create_without_commit(self, history: History) -> History:
        logger.debug("History - Repository - create_without_commit")
        id = uuid.uuid4()
        history.id = id
        self.db.add(history)
        self.db.commit()
        return history