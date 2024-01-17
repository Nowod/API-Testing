"""
req
.get
.params
.headers
.
"""
import requests
from response import Response


class Request:
    def __init__(self) -> None:
        self.__url = None
        self.__headers = None
        self.__version = None
        self.__body = None

    def headers(self, headers: dict) -> "Request":
        self.__headers = headers
        return self

    def body(self, body: dict) -> "Request":
        self.__body = body
        return self

    def get(self, url: str) -> "Response":
        self.__url = url
        _res = requests.get(self.__url)
        return Response(
            status_code=_res.status_code, headers=_res.headers, body=_res.text
        )

    def post(self, url: str, body: str) -> "Response":
        self.__url = url
        self.__body = body
        return Response

    def put(self, url: str, body: str) -> "Response":
        self.__url = url
        self.__body = body
        return Response

    def patch(self, url: str, body: str) -> "Response":
        self.__url = url
        self.__body = body
        return Response

    def delete(self, url: str) -> "Response":
        self.__url = url
        return Response


if __name__ == "__main__":
    req = Request()
    print(req.get("http://www.baidu.com").__dict__)
