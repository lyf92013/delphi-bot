from fastapi import APIRouter

from src import handler
from src.util.glossary import HttpMethod
from . import _order as order

router = APIRouter(prefix="/v1")
router.add_api_route(
    name="Ping",
    path="/ping",
    methods=[HttpMethod.GET],
    endpoint=handler.PingHandler(),
)
router.include_router(order.router, prefix="/order", tags=["order"])
