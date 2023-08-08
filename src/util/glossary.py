from enum import Enum


class HttpMethod(str, Enum):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"


class StatusCode(int, Enum):
    SUCCESS = 0
    WRONG_AUTH_KEY_ERROR = 1
    ADD_ORDER_ERROR = 2
    VALIDATION_ERROR = 3


class Trade(str, Enum):
    BUY = "buy"
    SELL = "sell"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
