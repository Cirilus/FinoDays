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


class CFA(EntityMeta):
    __tablename__ = "CFA"
    id = Column(UUID, primary_key=True)

    user_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    company_id = Column(UUID, ForeignKey("company.id"), nullable=False)

    count = Column(Integer)
    approved = Column(Boolean)
    price = Column(Float)
    date_release = Column(TIMESTAMP)
    payment_method = Column(String)
    subject = Column(String)
    moderated = Column(Boolean)
    token = Column(String)