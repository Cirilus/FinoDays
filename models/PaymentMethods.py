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

from models.BaseModel import EntityMeta


class PaymentMethods(EntityMeta):
    __tablename__ = "payment_methods"
    id = Column(UUID, primary_key=True)
    name = Column(String, nullable=False, unique=True)
