from models.BaseModel import EntityMeta
from sqlalchemy import (
    Column,
    UUID,
    Integer,
    String,
    PrimaryKeyConstraint,
    Boolean,
    Float,
    TIMESTAMP,
    ForeignKey
)

from sqlalchemy.orm import relationship


class User(EntityMeta):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True)

    company = Column(UUID, ForeignKey("company.id"))

    name = Column(String)
    surname = Column(String)
    middelname = Column(String)
    location = Column(String)
    registry = Column(String, unique=True)
    beneficial_owner = Column(String)

    def normalize(self):
        return {
            "id": self.id,
            "company": self.company,
            "name": self.name,
            "surname": self.surname,
            "middelname": self.middelname,
            "location": self.location,
            "registry": self.registry,
            "beneficial_owner": self.beneficial_owner
        }