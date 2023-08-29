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


class Company(EntityMeta):
    __tablename__ = "company"
    id = Column(UUID, primary_key=True)
    name = Column(String)

    relationship("CFA", back_populates="company")

    def normalize(self):
        return {
            "id": self.id,
            "name": self.name,
        }