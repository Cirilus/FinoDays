from models.User import User
from schemas.UserSchema import UserRequest

from models.cfa import CFA
from schemas.CFAchema import CFARequest


def CFARequestToCFA(cfa: CFARequest) -> CFA:
    result = CFA()

    result.user.id = cfa.user
    result.company.id = cfa.company

    result.count = cfa.count
    result.approved = cfa.approved
    result.price = cfa.price
    result.date_release = cfa.date_release
    result.payment_method = cfa.payment_method
    result.subject = cfa.subject
    result.moderated = cfa.moderated
    result.token = cfa.token

    return result

def UserRequestToUser(user: UserRequest) -> User:
    result = User()
    
    result.company.id = user.company
    
    result.id = user.id    
    result.login = user.login
    result.password_hashed = user.password_hashed
    result.company = user.company
    result.name = user.name
    result.surname = user.surname
    result.middelname = user.middelname
    result.location = user.location
    result.registry = user.registry
    result.beneficial_owner = user.beneficial_owner