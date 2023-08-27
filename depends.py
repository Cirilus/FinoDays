from repositories.CFA import CFARepository
from services.CFA import CFAService

CFA_repo = CFARepository()

CFA_service = CFAService(CFA_repo)


def get_cfa_services() -> CFAService:
    return CFA_service
