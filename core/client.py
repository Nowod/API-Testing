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

from requests import Request, Response, Session

from .exceptions import MethodError
from .validator import Validator


class Optional:
    def __init__(self, request: Request) -> None:
        self.__request: Request = request
        self.__session: Session = Session()

    def headers(self, headers: dict) -> "Optional":
        self.__request.headers = headers
        return self

    def body(self, payload: dict) -> "Optional":
        self.__request.data = payload
        return self

    def params(self, params: dict) -> "Optional":
        return self

    def send(self, timeout: int = 8) -> Validator:
        if self.__request.method is None:
            raise MethodError("The request method is not declared!")
        else:
            pre_request = self.__request.prepare()
            self.__response = self.__session.send(pre_request, timeout=timeout)
        return Validator(self.__request, self.__response)


class Client:
    def __init__(self) -> None:
        self.__request: Request = Request()
        self.__session: Session = Session()
        self.__response: Response | None = None

    def get(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "GET"
        return Optional(self.__request)

    def post(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "POST"
        return Optional(self.__request)

    def put(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "PUT"
        return Optional(self.__request)

    def patch(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "PATCH"
        return Optional(self.__request)

    def delete(self, url: str) -> "Optional":
        self.__request.url = url
        self.__request.method = "DELETE"
        return Optional(self.__request)
