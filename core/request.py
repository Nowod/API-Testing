"""
client
.import()
.get()
.headers()
.params()
.body()
.send()

.reveice(timeout=0)

.assert_header()
.assert_body(IMAGE/JSON/HTML)
.export
"""
import requests
from .enum import Method
from .response import Response
from .exceptions import MethodError


class Request:
    def __init__(self) -> None:
        self.__url = None
        self.__headers = None
        self.__version = None
        self.__params = None
        self.__body = None
        self.__method = None
        self.__response = None

    def _get_res(self):
        return self.__response

    def headers(self, headers: dict) -> "Request":
        self.__headers = headers
        return self

    def body(self, body: dict) -> "Request":
        self.__body = body
        return self

    def params(self, params: dict) -> "Request":
        self.__params = params
        return self

    def get(self, url: str) -> "Request":
        self.__url = url
        self.__method = Method.GET
        return self

    def post(self, url: str, body: str) -> "Request":
        self.__url = url
        self.__method = Method.POST
        self.__body = body
        return self

    def put(self, url: str, body: str) -> "Request":
        self.__url = url
        self.__method = Method.PUT
        self.__body = body
        return self

    def patch(self, url: str, body: str) -> "Request":
        self.__url = url
        self.__method = Method.PATCH
        self.__body = body
        return self

    def delete(self, url: str) -> "Request":
        self.__url = url
        self.__method = Method.DELETE
        return self

    def send(self, timeout: int = 8) -> "Response":
        if self.__method is None:
            raise MethodError("The request method is not declared!")
        elif self.__method == Method.GET:
            self.__response = requests.get(
                self.__url,
                params=self.__params,
                headers=self.__headers,
                timeout=timeout,
            )
        elif self.__method == Method.POST:
            self.__response = requests.post(
                self.__url, data=self.__body, headers=self.__headers, timeout=timeout
            )
        elif self.__method == Method.PUT:
            self.__response = requests.put(
                self.__url, data=self.__body, headers=self.__headers, timeout=timeout
            )
        elif self.__method == Method.PATCH:
            self.__response = requests.patch(
                self.__url, data=self.__body, headers=self.__headers, timeout=timeout
            )
        elif self.__method == Method.DELETE:
            self.__response = requests.delete(
                self.__url, headers=self.__headers, timeout=timeout
            )
        else:
            raise MethodError(
                "The request method[{}] does not exist".format(self.__method)
            )

        return Response(self.__response)
        # return _res


if __name__ == "__main__":
    req = Request()
    res = req.get("http://www.baidu.com").send(10)
    print(req._get_res().text)
