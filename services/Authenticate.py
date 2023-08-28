import uuid

from datetime import timedelta, datetime
from typing import Annotated

from jose import JWTError, jwt
from loguru import logger
from passlib.context import CryptContext
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from services.User import UserService
from utils.wrappers import error_wrapper
from schemas.Token import Token, TokenData


class AuthService:
    def __init__(self, user_service: UserService = Depends()):
        self.SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        self.ALGORITHM = "HS256"
        self.ACCESS_TOKEN_EXPIRE_MINUTES = 30

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.user_service = user_service
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def get_by_id(
            self,
            user_id: uuid.UUID,
            
    ):
        user = self.user_service.get_by_id(user_id)
        return user

    def get_by_login(
            self,
            login: str,
            
    ):
        user = self.user_service.get_by_login(login)
        return user

    def authenticate_user(
            self,
            login: str,
            password: str
    ):
        user = self.get_by_login(login)
        if not user:
            return False
        if not self.verify_password(password, user.password_hashed):
            return False
        return user

    def create_access_token(
            self,
            data: dict,
            expires_delta: timedelta | None = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def get_current_user(
            self,
            token
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(login=username)
        except JWTError:
            raise credentials_exception
        user = self.get_by_login(token_data.login)
        if user is None:
            raise credentials_exception
        return user

    def login_for_access_token(
            self,
            form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Token:
        user = self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={"sub": user.login}, expires_delta=access_token_expires
        )

        response = Token(access_token=access_token, token_type="bearer")

        return response
