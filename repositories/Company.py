from typing import List

from fastapi import Depends

from configs.Database import get_db_connection
from models.Company import Company
from sqlalchemy.orm import Session, lazyload


class CompanyRepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_companies(self) -> List[Company]:
        query = self.db.query(Company)
        return query.all()