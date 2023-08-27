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
