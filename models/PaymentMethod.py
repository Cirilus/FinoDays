from sqlalchemy import (
    Column,
    UUID,
    Integer,
    String,
    PrimaryKeyConstraint,
    Boolean,
    Float,
    TIMESTAMP, ForeignKey
)
from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta


class PaymentMethod(EntityMeta):
    __tablename__ = "payment_methods"
    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    cfa = relationship("CFA", backref="Payment_method")
    def normalize(self):
        return {
            "id": self.id,
            "name": self.name,
        }