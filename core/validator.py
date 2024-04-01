from requests import Request, Response

from .utils import extract_json


class RequestValidator:
    def __init__(self, request: Request) -> None:
        self.__request: Request = request


class ResponseValidator:
    def __init__(self, response: Response) -> None:
        self.__response: Response = response
        self.__body: str = response.text

    def assert_equal(self, actual: str, expect) -> None:
        assert extract_json(actual, self.__body) == expect

    def assert_not_equal(self, actual: str, expect) -> None:
        assert extract_json(actual, self.__body) != expect


class Validator(RequestValidator, ResponseValidator):
    def __init__(self, request: Request, response: Response) -> None:
        RequestValidator.__init__(self, request)
        ResponseValidator.__init__(self, response)
