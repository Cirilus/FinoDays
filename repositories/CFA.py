from typing import List

from fastapi import Depends

from configs.Database import get_db_connection
from models.cfa import CFA
from sqlalchemy.orm import Session, lazyload


class CFARepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_cfas(self) -> List[CFA]:
        query = self.db.query(CFA)
        return query.all()
