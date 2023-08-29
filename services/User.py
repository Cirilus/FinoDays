from typing import List

import uuid
from fastapi import Depends
from loguru import logger
from passlib.context import CryptContext

from repositories.User import UserRepository
from models.User import User


class UserService:
    def __init__(self,
                 user_repo: UserRepository = Depends()):
        logger.debug(user_repo)
        self.user_repo = user_repo
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_list(self, limit: int, offset: int) -> List[User]:
        logger.debug("User - Service - get_users")
        result = self.user_repo.get_list(limit, offset)
        return result

    def get_by_id(self, id: uuid.UUID) -> User:
        logger.debug("User - Service - get_user_by_id")
        result = self.user_repo.get_by_id(id)
        return result

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def get_by_login(self, login: str) -> User:
        logger.debug("User - Service get_user_by_login")
        result = self.user_repo.get_by_login(login)
        return result

    def delete(self, id: uuid.UUID) -> None:
        logger.debug("User - Service - delete_user")

        user = self.user_repo.get_by_id(id)

        self.user_repo.delete(user)
        return None

    def update(self, id: uuid.UUID, user: User) -> User:
        logger.debug("User - Service - update_user")
        result = self.user_repo.update(id, user)
        return result

    def create(self, user: User) -> User:
        logger.debug("User - Service - update_user")
        user.password_hashed = self.get_password_hash(user.password_hashed)
        result = self.user_repo.create(user)
        return result
