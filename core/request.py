"""
req
.get
.params
.headers
.
"""
import requests


class GetMethod:
    def __init__(self) -> None:
        self.url = None
        self.headers = None
        self.data = None

    def headers(self, headers) -> "GetMethod":
        self.headers = headers
        return self

    def get(self, url) -> "GetMethod":
        self.url = url
        return self


class Request:
    def __init__(self) -> None:
        self.url = None
        self.method = None
        self.headers = None
        self.data = None

    def headers(self, headers) -> "Request":
        self.headers = headers
        return self

    def get(self, url) -> "Request":
        self.method = "GET"
        self.url = url
        return self

    def post(self, url, data) -> "Request":
        self.method = "POST"
        self.url = url
        self.data = data
        return self
