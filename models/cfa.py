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


class CFA(EntityMeta):
    __tablename__ = "cfa"
    id = Column(UUID, primary_key=True)

    user_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    company_id = Column(UUID, ForeignKey("company.id"), nullable=False)

    count = Column(Integer)
    approved = Column(Boolean)
    price = Column(Float)
    date_release = Column(TIMESTAMP)
    payment_method = Column(UUID, ForeignKey("payment_methods.id"), nullable=True)
    subject = Column(String)
    moderated = Column(Boolean)
    token = Column(String)

    def normalize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "company_id": self.company_id,
            "count": self.count,
            "approved": self.approved,
            "price": self.price,
            "date_release": self.date_release,
            "payment_method": self.payment_method,
            "subject": self.subject,
            "moderated": self.moderated,
            "token": self.token
        }