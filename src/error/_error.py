from typing import Any, Optional

from pydantic import validate_arguments

from src.util.glossary import StatusCode


class Error(Exception):
    """
    Base class for all errors.
    """

    @validate_arguments
    def __init__(
        self,
        *,
        code: int,
        message: Any = None,
    ) -> None:
        super().__init__()
        self.code = code
        self.message = message


class WrongAuthKeyError(Error):
    def __init__(self) -> None:
        super().__init__(
            code=StatusCode.WRONG_AUTH_KEY_ERROR,
            message="Auth key is wrong.",
        )


class ValidationError(Error):
    def __init__(self, message: Any) -> None:
        super().__init__(
            code=StatusCode.VALIDATION_ERROR,
            message=message,
        )


class AddOrderError(Error):
    def __init__(self, message: str) -> None:
        super().__init__(
            code=StatusCode.ADD_ORDER_ERROR,
            message=message,
        )
