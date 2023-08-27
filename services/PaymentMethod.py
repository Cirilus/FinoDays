from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from repositories.PaymentMethod import PaymentMethodRepository
from models.PaymentMethod import PaymentMethod
from utils.errors import ErrEntityNotFound, ErrEntityConflict


class PaymentMethodServices:
    def __init__(self, payment_repo: PaymentMethodRepository = Depends()) -> None:
        self.payment_repo = payment_repo

    def get_list(
            self,
    ) -> List[PaymentMethod]:
        logger.debug("PaymentMethodRepository - Service - get_list")
        result = self.payment_repo.get_list()
        return result

    def get_by_id(self, id: uuid.UUID) -> PaymentMethod:
        logger.debug("PaymentMethodRepository - Service - get_by_id")
        result = self.payment_repo.get_by_id(id)
        return result

    def delete(self, id: uuid.UUID) -> None:
        logger.debug("PaymentMethodRepository - Service - delete")

        payment = self.payment_repo.get_by_id(id)

        self.payment_repo.delete(payment)
        return None

    def update(self, id: uuid.UUID, payment: PaymentMethod) -> PaymentMethod:
        logger.debug("PaymentMethodRepository - Service - update")

        if self.payment_repo.get_by_name(payment.name) is not None:
            raise ErrEntityConflict("the field name must ne unique")

        if not self.payment_repo.get_by_id(id):
            raise ErrEntityNotFound("the entity not found")

        result = self.payment_repo.update(id, payment)
        return result
    
    def create(self, payment: PaymentMethod) -> PaymentMethod:
        logger.debug("PaymentMethodRepository - Service - update")

        if self.payment_repo.get_by_name(payment.name) is not None:
            raise ErrEntityConflict("the field name must ne unique")
        
        result = self.payment_repo.create(payment)
        return result
