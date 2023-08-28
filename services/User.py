from typing import List

import uuid
from fastapi import Depends
from loguru import logger

from repositories.User import UserRepository
from models.User import User


class UserService:
    def __init__(self, User_repo: UserRepository = Depends()) -> None:
        self.User_repo = User_repo

    def get_list(self, limit: int, offset: int) -> List[User]:
        logger.debug("User - Service - get_users")
        result = self.User_repo.get_list(limit, offset)
        return result

    def get_by_id(self, id: uuid.UUID) -> User:
        logger.debug("User - Service - get_user_by_id")
        result = self.User_repo.get_by_id(id)
        return result
    
    def get_by_login(self, login: str) -> User:
        logger.debug("User - Service get_user_by_login")
        result = self.User_repo.get_by_login(login)
        return result

    def delete(self, id: uuid.UUID) -> None:
        logger.debug("User - Service - delete_user")

        User = self.User_repo.get_by_id(id)

        self.User_repo.delete(User)
        return None

    def update(self, id: uuid.UUID, User: User) -> User:
        logger.debug("User - Service - update_user")
        result = self.User_repo.update(id, User)
        return result

    def create(self, User: User) -> User:
        logger.debug("User - Service - update_user")
        result = self.User_repo.create(User)
        return result