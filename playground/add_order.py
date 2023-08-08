from binance.um_futures import UMFutures


key = "7af10e3f1edc4fd2ad0c2a6586d3aee6f87aeab1b64b1311fcc92a1f8b64c6d4"
secret = "b13408e51f5e4f76ab5e5a26adaa626e1b4bd0b2ce2cd3537d19b24d79912162"
um_futures_client = UMFutures(
    base_url="https://testnet.binancefuture.com", key=key, secret=secret
)


# Post a new order
params = {
    "symbol": "ETHUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.01,
}

response = um_futures_client.new_order(**params, recvWindow=10000)
# print(response)
