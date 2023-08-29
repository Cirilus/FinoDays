from datetime import datetime

from sqlalchemy import (
    Column,
    UUID,
    Integer,
    String,
    PrimaryKeyConstraint,
    Boolean,
    Float,
    TIMESTAMP, ForeignKey, DateTime, UniqueConstraint
)

from models.BaseModel import EntityMeta


class History(EntityMeta):
    __tablename__ = "history"
    id = Column(UUID, primary_key=True)
    seller = Column(UUID, ForeignKey("user.id"), nullable=True)
    recipient = Column(UUID, ForeignKey("user.id"), nullable=False)
    cfa = Column(UUID, ForeignKey("cfa.id"), nullable=False)
    count = Column(Integer)
    price = Column(Float)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('seller', 'recipient', name='_seller_recipient_uc'),
    )
