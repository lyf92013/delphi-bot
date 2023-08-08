from fastapi import APIRouter

from src import handler
from src.util.glossary import HttpMethod

router = APIRouter()

router.add_api_route(
    name="Order",
    description="Add Order",
    path="",
    methods=[HttpMethod.POST],
    endpoint=handler.AddOrderHandler().__call__,
)
