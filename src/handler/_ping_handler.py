from ._base_handler import BaseHandler


class PingHandler(BaseHandler):
    def __call__(self) -> str:
        return "pong"
