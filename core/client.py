"""
client
.import()
.get()
.headers()
.params()
.body()
.send(timeout=0)

.assert_header()
.assert_body(IMAGE/JSON/HTML)
.export
"""

import json
from typing import Mapping

from requests import Request, Session

from .exceptions import MethodError
from .utils import deep_traverse_and_format
from .validator import ResponseValidator


class Optional:
    def __init__(self, request: Request, extract: Mapping) -> None:
        self.__request: Request = request
        self.__session: Session = Session()
        self.__extract: dict = extract

    def headers(self, headers: Mapping) -> "Optional":
        self.__request.headers = headers
        return self

    def body(self, payload: str) -> "Optional":
        # TODO x-www-form-urlencode
        # TODO multipart/form-data --- use requests-toolbelt lib
        # TODO application/json
        self.__request.json = json.dumps(
            deep_traverse_and_format(json.loads(payload), self.__extract)
        )
        return self

    def params(self, params: Mapping) -> "Optional":
        return self

    def send(self, timeout: int = 8) -> ResponseValidator:
        if self.__request.method is None:
            raise MethodError("The request method is not declared!")
        else:
            pre_request = self.__request.prepare()
            self.__response = self.__session.send(pre_request, timeout=timeout)

        return ResponseValidator(response=self.__response, extract=self.__extract)


class Client:
    def __init__(self) -> None:
        self.__request: Request = Request()
        # self.__session: Session = Session()
        # self.__response: Response | None = None
        self.__extract: dict = {}

    def _set_extract(self, extract: Mapping) -> "Client":
        self.__extract = extract
        return self

    def get(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "GET"
        return Optional(self.__request, self.__extract)

    def post(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "POST"
        return Optional(self.__request, self.__extract)

    def put(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "PUT"
        return Optional(self.__request, self.__extract)

    def patch(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "PATCH"
        return Optional(self.__request, self.__extract)

    def delete(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "DELETE"
        return Optional(self.__request, self.__extract)
