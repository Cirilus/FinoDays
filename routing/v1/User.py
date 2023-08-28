import http
from typing import List, Optional

import uuid
from fastapi import APIRouter, Depends
from loguru import logger
from starlette.responses import JSONResponse

from utils.errors import ErrEntityNotFound
from schemas.UserSchema import UserRequest, UserSchema
from services.User import UserService
from convertors.User import UserRequestToUser
from utils.wrappers import error_wrapper

router = APIRouter(prefix="/api/v1/user", tags=["user"])


@router.get(
    "",
    response_model=List[UserSchema],
    description="get all users",
)
async def get_list(
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        User_service: UserService = Depends()
):
    logger.debug("User - Route - get_users")
    User = error_wrapper(User_service.get_list,
                        limit, offset)
    return User


@router.get(
    "/{user_id}",
    response_model=UserSchema,
    description="get user by uuid",
)
async def get_by_id(
        User_id: uuid.UUID,
        User_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")
    User = error_wrapper(User_service.get_by_id, User_id)
    return User


@router.patch(
    "/{user_id}",
    response_model=UserSchema,
    description="update user",
)
async def update(
        User_id: uuid.UUID,
        User_request: UserRequest,
        User_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")

    User = UserRequestToUser(User_request)
    User = error_wrapper(User_service.update, User_id, User)
    return User


@router.delete(
    "/{user_id}",
    responses={200: {"msg": "successfully deleted"}},
    description="delete user",
)
async def delete(
        User_id: uuid.UUID,
        User_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")
    response = error_wrapper(User_service.delete, User_id)
    if not response:
        response = JSONResponse(status_code=http.HTTPStatus.OK, content={"msg": "successfully deleted"})
    return response


@router.post(
    "",
    response_model=UserSchema,
    description="create User",
)
async def create(
        User_request: UserRequest,
        User_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")

    User = UserRequestToUser(User_request)

    error_wrapper(User_service.create, User)

    return User
