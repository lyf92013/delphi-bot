from fastapi.exceptions import RequestValidationError
import uvicorn
from fastapi import FastAPI
from src.container import Container
from src.router import v1
from src.error import Error
from src.handler import exception_handler, validation_exception_handler

app = FastAPI()
container = Container()
app.container = container
container.wire(
    modules=[
        ".handler",
    ],
    from_package="src",
)
container.init_resources()

app.include_router(v1.router, prefix="/api")
app.add_exception_handler(Error, exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, reload_dirs=["."])
