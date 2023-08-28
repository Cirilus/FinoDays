import http
from typing import List, Optional, Annotated

import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from loguru import logger
from starlette.responses import JSONResponse
from jose import JWTError, jwt
from passlib.context import CryptContext


from utils.errors import ErrEntityNotFound
from schemas.UserSchema import UserRequest, UserSchema
from services.User import UserService
from services.Authenticate import AuthService
from convertors.User import UserRequestToUser
from utils.wrappers import error_wrapper
from schemas.Token import Token, TokenData


router = APIRouter(prefix="/api/v1/user", tags=["user"])


@router.get(
    "",
    response_model=List[UserSchema],
    description="get all users",
)
async def get_list(
        limit: Optional[int] = 100,
        offset: Optional[int] = 0,
        user_service: UserService = Depends()
):
    logger.debug("User - Route - get_users")
    user = error_wrapper(user_service.get_list,
                        limit, offset)
    return user


@router.get(
    "/{user_id}",
    response_model=UserSchema,
    description="get user by uuid",
)
async def get_by_id(
        user_id: uuid.UUID,
        user_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")
    user = error_wrapper(user_service.get_by_id, user_id)
    return user


@router.get(
    "/me",
    response_model=UserSchema,
    description="get current user"
)
async def get_current_user(
        auth_service: AuthService = Depends()
):
    logger.debug("User - Route get_current_user")
    user = error_wrapper(auth_service.get_current_user)
    return user


@router.patch(
    "/{user_id}",
    response_model=UserSchema,
    description="update user",
)
async def update(
        user_id: uuid.UUID,
        user_request: UserRequest,
        user_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")

    user = UserRequestToUser(user_request)
    user = error_wrapper(user_service.update, user_id, user)
    return user


@router.delete(
    "/{user_id}",
    responses={200: {"msg": "successfully deleted"}},
    description="delete user",
)
async def delete(
        user_id: uuid.UUID,
        user_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")
    response = error_wrapper(user_service.delete, user_id)
    if not response:
        response = JSONResponse(status_code=http.HTTPStatus.OK, content={"msg": "successfully deleted"})
    return response


@router.post(
    "",
    response_model=UserSchema,
    description="create User",
)
async def create(
        user_request: UserRequest,
        user_service: UserService = Depends()
):
    logger.debug("User - Route - get_user_by_id")

    user = UserRequestToUser(user_request)

    error_wrapper(user_service.create, user)

    return user

@router.post(
    "/token", 
    response_model=Token,
    description="get access token by login in")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: AuthService = Depends()
):
    logger.debug("User - Route - login_for_access_token")
    resp = error_wrapper(auth_service.login_for_access_token, form_data)
    
    return resp

