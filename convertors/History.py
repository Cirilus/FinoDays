from models.History import History
from schemas.History import HistoryRequest


def HistoryRequestToHistory(history: HistoryRequest) -> History:
    result = History()

    result.id = history.id
    result.seller = history.seller
    result.recipient = history.recipient
    result.cfa = history.cfa
    result.count = history.count
    result.price = history.price
    result.created_at = history.created_at

    return result
