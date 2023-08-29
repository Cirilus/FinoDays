from loguru import logger

from models.cfa import CFA
from schemas.CFASchema import CFARequest, CFASchema


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


def CFAToCFASchema(cfa: CFA) -> CFASchema:
    result = CFASchema(
        id=cfa.id,
        user=cfa.user.normalize(),
        company=cfa.company.normalize(),
        payment_method=cfa.Payment_method.normalize(),
        count=cfa.count,
        approved=cfa.approved,
        price=cfa.price,
        date_release=cfa.date_release,
        subject=cfa.subject,
        moderated=cfa.moderated,
        token=cfa.token,
    )

    return result
