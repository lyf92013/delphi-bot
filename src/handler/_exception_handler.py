from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import UJSONResponse, UJSONResponse
from loguru import logger
from src.util.glossary import StatusCode

from src.error import Error
from src.schema import ResponseData


async def exception_handler(_, exc: Error):  # no issue reported on _
    return UJSONResponse(
        content=ResponseData(
            code=exc.code,
            message=exc.message,
            error=exc.__class__.__name__,
        ).dict(exclude={"data"}),
        status_code=status.HTTP_400_BAD_REQUEST,
    )


async def validation_exception_handler(_, exc: RequestValidationError):
    logger.error(exc)
    return UJSONResponse(
        content=ResponseData(
            code=StatusCode.VALIDATION_ERROR,
            message=str(exc),
            error=exc.__class__.__name__,
        ).dict(exclude={"data"}),
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )
