import uuid
from typing import List

from fastapi import Depends

from configs.Database import get_db_connection
from models.PaymentMethod import PaymentMethod
from sqlalchemy.orm import Session
from utils.errors import ErrEntityNotFound


class PaymentMethodRepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_list(self) -> List[PaymentMethod]:
        query = self.db.query(
            PaymentMethod
        ).all()
        return query

    def get_by_id(self, id: uuid.UUID) -> PaymentMethod:
        payment_method = self.db.get(
            PaymentMethod,
            id
        )

        if payment_method is None:
            raise ErrEntityNotFound("entity not found")

        return payment_method

    def get_by_name(self, name: str) -> PaymentMethod:
        payment_method = self.db.query(
            PaymentMethod,
        ).filter(PaymentMethod.name==name).first()
        return payment_method

    def create(self, payment_method: PaymentMethod) -> PaymentMethod:
        id = uuid.uuid4()
        payment_method.id = id
        self.db.add(payment_method)
        self.db.commit()
        self.db.refresh(payment_method)
        return payment_method

    def update(self, id: uuid.UUID, payment_method: PaymentMethod) -> PaymentMethod:
        payment_method.id = id
        self.db.merge(payment_method)
        self.db.commit()
        return payment_method

    def delete(self, payment_method: PaymentMethod) -> None:
        self.db.delete(payment_method)
        self.db.commit()
        self.db.flush()
