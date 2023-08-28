from models.cfa import CFA
from schemas.CFA import CFARequest

def CFARequestCreateToCFA(cfa: CFARequest) -> CFA:
    result = CFA()

    result.user_id = cfa.user_id
    result.company_id = cfa.company_id
    result.count = cfa.count
    result.approved = cfa.approved
    result.price = cfa.price
    result.date_release = cfa.date_release
    result.payment_method = cfa.payment_method
    result.subject = cfa.subject
    result.moderated = cfa.moderated
    result.token = cfa.token
    return result
