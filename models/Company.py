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


class Company(EntityMeta):
    __tablename__ = "company"
    id = Column(UUID, primary_key=True)
    name = Column(String)
