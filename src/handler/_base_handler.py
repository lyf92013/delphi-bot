from dataclasses import is_dataclass
from typing import Any

from fastapi import status
from fastapi.responses import UJSONResponse
from pydantic import validate_arguments
from starlette.responses import RedirectResponse

from src.schema import ResponseData
from src.util.convert import to_camel_case
from src.util.glossary import StatusCode


class BaseHandler:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError

    @validate_arguments
    def response(
        self,
        data: Any = None,
        redirect_uri=None,
    ) -> UJSONResponse | RedirectResponse:
        response = (
            RedirectResponse(url=redirect_uri, status_code=status.HTTP_302_FOUND)
            if redirect_uri
            else UJSONResponse(
                content=ResponseData(
                    code=StatusCode.SUCCESS,
                    message="success",
                    data=self._serialize(data),
                ).dict(
                    exclude={"error"},
                    exclude_none=True,
                    exclude_unset=True,
                ),
                status_code=status.HTTP_200_OK,
            )
        )

        return response

    def _serialize(self, data: Any) -> Any:
        if is_dataclass(data):
            result = {}
            for key, value in data.__dataclass_fields__.items():
                if is_dataclass(getattr(data, key)):
                    result[key] = self._serialize(getattr(data, key))
                elif "ignore" not in value.metadata or not value.metadata["ignore"]:
                    result[key] = getattr(data, key)
            return self._to_camel_case(result)

        return self._to_camel_case(data)

    @validate_arguments
    def _to_camel_case(self, data: dict | list | str | None) -> Any:
        if isinstance(data, dict):
            return {to_camel_case(key): value for key, value in data.items()}

        if isinstance(data, list):
            return [to_camel_case(datum) for datum in data]

        return to_camel_case(data)
