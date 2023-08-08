from typing import Any, Optional

from pydantic import BaseModel


class ResponseData(BaseModel):
    code: int
    error: Optional[str]
    message: str
    data: Any
