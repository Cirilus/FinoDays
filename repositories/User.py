from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from configs.Database import get_db_connection
from utils.errors import ErrEntityNotFound
from models.User import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get_list(self, limit: int, offset: int) -> List[User]:
        logger.debug("User - Repository - get_list")
        query = self.db.query(User)
        return query.offset(offset).limit(limit).all()

    def get_by_id(self, id: uuid.UUID) -> User:
        logger.debug("User - Repository - get_by_id")
        user = self.db.get(User, id)

        if user is None:
            raise ErrEntityNotFound("entity not found")
        return user
    
    def get_by_login(self, login: str) -> User:
        logger.debug("User - REpository get_by_login")
        user = self.db.get(User, login)
        
        if user is None:
            raise ErrEntityNotFound("entity not found")
        return user

    def create(self, user: User) -> User:
        logger.debug("User - Repository - create")
        id = uuid.uuid4()
        user.id = id
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, id: uuid.UUID, user: User) -> User:
        logger.debug("User - Repository - update")
        user.id = id
        self.db.merge(user)
        self.db.commit()
        return user

    def delete(self, user: User) -> None:
        logger.debug("User - Repository - delete")
        self.db.delete(user)
        self.db.commit()
        self.db.flush()