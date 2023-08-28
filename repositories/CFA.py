from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from configs.Database import get_db_connection
from models.Company import Company
from models.PaymentMethod import PaymentMethod
from models.User import User
from utils.errors import ErrEntityNotFound
from models.cfa import CFA
from sqlalchemy.orm import Session


class CFARepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_list(self, limit: int, offset: int, moderated: bool, payment_method: str) -> List[CFA]:
        logger.debug("CFA - Repository - get_list")
        query = self.db.query(CFA)
        if moderated:
            query.filter_by(moderated=moderated)
        if payment_method:
            query.filter_by(payment_method=payment_method)
        return query.offset(offset).limit(limit).all()

    def get_by_id(self, id: uuid.UUID) -> CFA:
        logger.debug("CFA - Repository - get_by_id")
        query = (
            self.db.query(CFA)
            .join(User, User.id == CFA.user_id)
            .join(Company, Company.id == CFA.company_id)
            .join(PaymentMethod, PaymentMethod.id == CFA.payment_method)
            .filter(CFA.user_id == id)
        )

        cfa = query.first()

        logger.debug(cfa)

        if cfa is None:
            raise ErrEntityNotFound("entity not found")

        return cfa

    def create(self, cfa: CFA) -> CFA:
        logger.debug("CFA - Repository - create")

        self.db.add(cfa)
        self.db.commit()
        self.db.refresh(cfa)
        return cfa

    def update(self, id: uuid.UUID, cfa: CFA) -> CFA:
        logger.debug("CFA - Repository - update")
        cfa.id = id
        self.db.merge(cfa)
        self.db.commit()
        return cfa

    def delete(self, cfa: CFA) -> None:
        logger.debug("CFA - Repository - delete")
        self.db.delete(cfa)
        self.db.commit()
        self.db.flush()
