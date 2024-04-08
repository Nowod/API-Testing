from requests import Response

from .exceptions import ExporterError
from .utils import extract_json


class Exporter:
    def __init__(self, response: Response, extract:dict) -> None:
        self.__response: Response = response
        self.__extract: dict = extract

    def export(self, source: str, target: str, alias: str) -> "Exporter":
        if source == "header":
            if target not in self.__response.headers:
                raise ExporterError(f"Header {target} not in {self.__response.headers}")
            extract_result = self.__response.headers[target]
        elif source == "body":
            extract_result = extract_json(target, self.__response.text)
            if not extract_result:
                raise ExporterError(f"Body {target} not in {self.__response.text}")
        elif source == "cookie":
            if target not in self.__response.cookies:
                raise ExporterError(f"Cookie {target} not in {self.__response.cookies}")
            extract_result = self.__response.cookies[target]
        else:
            raise ExporterError(
                f"Error source {source}, only support header, body, cookie"
            )
        self.__extract[alias] = extract_result
        return self
