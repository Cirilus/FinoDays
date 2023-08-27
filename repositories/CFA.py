from typing import List

from fastapi import Depends
from loguru import logger

from configs.Database import get_db_connection
from models.cfa import CFA
from sqlalchemy.orm import Session, lazyload


class CFARepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_cfas(self, limit: int, offset: int, moderated: bool, payment_method: str) -> List[CFA]:
        logger.debug("CFA - Repository - get_cfas")
        query = self.db.query(CFA)
        if moderated:
            query.filter_by(moderated=moderated)
        if payment_method:
            query.filter_by(payment_method=payment_method)
        return query.offset(offset).limit(limit).all()
