from binance.um_futures import UMFutures
import binance
import cryptography
from dependency_injector.wiring import Provide
from src import error
from fastapi import Request
from pydantic import BaseModel, Field
from src.util.cipher import Cipher
from src.util.glossary import Trade, OrderType

from ._base_handler import BaseHandler


class AddOrderHandler(BaseHandler):
    cipher: Cipher = Provide("cipher")

    class Param(BaseModel):
        key: str = Field(title="Auth Key")
        symbol: str = Field(title="Coin Symbol")
        trade: Trade = Field(
            title="Buy or Sell order",
        )
        type: OrderType = Field(title="Market or Limit")
        quantity: float = Field(title="Quantity")

    def __call__(self, _: Request, param: Param):
        try:
            api = self.cipher.decrypt(param.key)
            client = UMFutures(
                base_url="https://testnet.binancefuture.com",
                key=api.key,
                secret=api.secret,
            )
            client.new_order(
                symbol=param.symbol,
                side=param.trade.upper(),
                type=param.type,
                quantity=param.quantity,
                recvWindow=10000,
            )
            return self.response()
        except cryptography.fernet.InvalidToken:
            raise error.WrongAuthKeyError
        except binance.error.ClientError as e:
            raise error.AddOrderError(str(e.error_message))
