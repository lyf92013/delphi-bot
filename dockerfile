FROM python:3.11-alpine AS builder

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install -U pip setuptools wheel
RUN pip install pdm
COPY pyproject.toml pdm.lock README.md /project/
WORKDIR /project
RUN mkdir __pypackages__ && pdm install

FROM python:3.11-alpine

ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs
COPY . /project
WORKDIR /project

CMD ["python", "main.py"]
