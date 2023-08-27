from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from configs.Database import get_db_connection
from errors.errors import ErrEntityNotFound
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

    def get_cfa_by_id(self, id: uuid.UUID) -> CFA:
        logger.debug("CFA - Repository - get_cfa_by_id")
        cfa = self.db.get(CFA, id)

        if cfa is None:
            raise ErrEntityNotFound("entity not found")
        return cfa

    def create_cfa(self, cfa: CFA) -> CFA:
        self.db.add(CFA)
        self.db.commit()
        self.db.refresh(cfa)
        return cfa

    def update_cfa(self, id: uuid.UUID, cfa: CFA) -> CFA:
        cfa.id = id
        self.db.merge(cfa)
        self.db.commit()
        return cfa

    def delete_cfa(self, id: uuid.UUID) -> None:
        cfa = self.get_cfa_by_id(id)
        self.db.delete(cfa)
        self.db.commit()
        self.db.flush()
