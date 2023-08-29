from models.User import User
from schemas.UserSchema import UserRequest, UserResponse


def UserRequestToUser(user: UserRequest) -> User:
    result = User()

    result.company = user.company
    result.login = user.login
    result.password_hashed = user.password_hashed
    result.company = user.company
    result.name = user.name
    result.surname = user.surname
    result.middelname = user.middelname
    result.location = user.location
    result.registry = user.registry
    result.beneficial_owner = user.beneficial_owner

    return result


def UserToUserReponse(user: User) -> UserResponse:
    result = User()

    result.company = user.company
    result.login = user.login
    result.password_hashed = user.password_hashed
    result.company = user.company
    result.name = user.name
    result.surname = user.surname
    result.middelname = user.middelname
    result.location = user.location
    result.registry = user.registry
    result.beneficial_owner = user.beneficial_owner

    return result