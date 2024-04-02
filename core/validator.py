import re
from typing import Type, Union

from jsonschema import validate as jsonschema_validate
from pydantic import ValidationError
from requests import Request, Response

from .utils import extract_json


class RequestValidator:
    def __init__(self, request: Request) -> None:
        self.__request: Request = request


class ResponseValidator:
    def __init__(self, response: Response) -> None:
        self.__response: Response = response
        self.__body = self.__response.text
        self.__headers: dict = self.__response.headers

    def assert_status_code(self, status_code: int) -> "ResponseValidator":
        assert self.__response.status_code == status_code
        return self

    def assert_header(self, key: str, value: str) -> "ResponseValidator":
        assert self.__headers[key] == value
        return self

    def assert_timing(self, timing: Union[int, float]) -> "ResponseValidator":
        assert self.__response.elapsed.total_seconds() <= timing
        return self

    # assert exist
    def assert_exist(self, actual: str) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result
        return self

    def assert_not_exist(self, actual: str) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert not extract_result
        return self

    # assert value
    def assert_equal(self, actual: str, expect) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result == expect
        return self

    def assert_not_equal(self, actual: str, expect) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result != expect
        return self

    def assert_greater_than(self, actual: str, expect: int) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result > expect
        return self

    def assert_less_than(self, actual: str, expect: int) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result < expect
        return self

    def assert_greater_or_equal(self, actual: str, expect: int) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result >= expect

    def assert_less_or_equal(self, actual: str, expect: int) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result <= expect
        return self

    # assert contain
    def assert_contains(self, actual: str, expect) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert expect in extract_result
        return self

    def assert_not_contains(self, actual: str, expect) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert expect not in extract_result
        return self

    def assert_in(self, actual: str, expect) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result in expect
        return self

    def assert_not_in(self, actual: str, expect) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert extract_result not in expect
        return self

    # assert format
    def assert_schema(self, actual: str, schema: dict) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        try:
            jsonschema_validate(instance=extract_result, schema=schema)
            return self
        except ValidationError as error:
            raise error

    def assert_pydantic(self, actual: str, model: Type) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        try:
            model(**extract_result)
        except ValidationError as e:
            raise e
        return self

    def assert_regex(self, actual: str, regex: str) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        match = re.match(regex, extract_result)
        if not match:
            raise AssertionError(f"Actual: {actual} does not match regex: {regex}")
        return self

    # assert type
    def assert_type(self, actual: str, expect: object) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        assert isinstance(extract_result, expect)
        return self

    def assert_object(self, actual: str) -> "ResponseValidator":
        self.assert_type(actual, dict)
        return self

    def assert_array(self, actual: str) -> "ResponseValidator":
        self.assert_type(actual, list)
        return self

    def assert_number(self, actual: str) -> "ResponseValidator":
        self.assert_type(actual, int)
        return self

    def assert_string(self, actual: str) -> "ResponseValidator":
        self.assert_type(actual, str)
        return self

    def assert_boolean(self, actual: bool) -> "ResponseValidator":
        self.assert_type(actual, bool)
        return self

    def assert_null(self, actual: str) -> "ResponseValidator":
        self.assert_type(actual, type(None))
        return self


# class Validator(RequestValidator, ResponseValidator):
#     def __init__(self, request: Request, response: Response) -> "ResponseValidator":
#         RequestValidator.__init__(self, request)
#         ResponseValidator.__init__(self, response)
