import re
from typing import Any, Type, Union

from jsonschema import validate as js_validate
from requests import Request, Response

from .exceptions import ValidatorError
from .utils import extract_json


class RequestValidator:
    def __init__(self, request: Request) -> None:
        self.__request: Request = request


class ResponseValidator:
    def __init__(self, response: Response) -> None:
        self.__response: Response = response
        self.__body = self.__response.text

    def assert_status_code(self, status_code: int) -> "ResponseValidator":
        if not self.__response.status_code == status_code:
            raise ValidatorError(
                f"Expect status code {status_code}, but got {self.__response.status_code}"
            )
        return self

    def assert_header(self, key: str, value: str) -> "ResponseValidator":
        if not self.__response.headers[key] == value:
            raise ValidatorError(
                f"Expect header {key} with value {value}, but got {self.__response.headers[key]}"
            )
        return self

    def assert_timing(self, timing: Union[int, float]) -> "ResponseValidator":
        if not self.__response.elapsed.total_seconds() <= timing:
            raise ValidatorError(
                f"Expect timing {timing}, but got {self.__response.elapsed.total_seconds()}"
            )
        return self

    # assert exist
    def assert_exist(self, actual: str) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result:
            raise ValidatorError(f"Actual: {actual} does not exist")
        return self

    def assert_not_exist(self, actual: str) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if extract_result:
            raise ValidatorError(f"Actual: {actual} exists")
        return self

    # assert value
    def assert_equal(
        self, actual: str, expect: Union[int, float]
    ) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result == expect:
            raise ValidatorError(f"Actual: {actual} does not equal to {expect}")
        return self

    def assert_not_equal(
        self, actual: str, expect: Union[int, float]
    ) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result != expect:
            raise ValidatorError(f"Actual: {actual} equals to {expect}")
        return self

    def assert_greater_than(
        self, actual: str, expect: Union[int, float]
    ) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result > expect:
            raise ValidatorError(f"Actual: {actual} does not greater than {expect}")
        return self

    def assert_less_than(
        self, actual: str, expect: Union[int, float]
    ) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result < expect:
            raise ValidatorError(f"Actual: {actual} does not less than {expect}")
        return self

    def assert_greater_or_equal(
        self, actual: str, expect: Union[int, float]
    ) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result >= expect:
            raise ValidatorError(
                f"Actual: {actual} does not greater or equal than {expect}"
            )
        return self

    def assert_less_or_equal(
        self, actual: str, expect: Union[int, float]
    ) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not extract_result <= expect:
            raise ValidatorError(
                f"Actual: {actual} does not less or equal than {expect}"
            )
        return self

    # assert contain
    def assert_contains(self, actual: str, expect: Any) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if expect not in extract_result:
            raise ValidatorError(f"Actual: {actual} does not contain {expect}")
        return self

    def assert_not_contains(self, actual: str, expect: Any) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if expect in extract_result:
            raise ValidatorError(f"Actual: {actual} contains {expect}")
        return self

    def assert_in(self, actual: str, expect: Any) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if extract_result not in expect:
            raise ValidatorError(f"Actual: {actual} does not in {expect}")
        return self

    def assert_not_in(self, actual: str, expect: Any) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if extract_result in expect:
            raise ValidatorError(f"Actual: {actual} in {expect}")
        return self

    # assert format
    def assert_schema(self, actual: str, schema: dict) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        try:
            js_validate(instance=extract_result, schema=schema)
        except Exception as error:
            raise ValidatorError("Invalid JSON schema") from error
        return self

    def assert_pydantic(self, actual: str, model: Type) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        try:
            model(**extract_result)
        except Exception as error:
            raise ValidatorError("Invalid Pydantic model") from error
        return self

    def assert_regex(self, actual: str, regex: str) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        match = re.match(regex, extract_result)
        if not match:
            raise ValidatorError(f"Actual: {actual} does not match regex: {regex}")
        return self

    # assert type
    def assert_type(self, actual: str, expect: object) -> "ResponseValidator":
        extract_result = extract_json(actual, self.__body)
        if not isinstance(extract_result, expect):
            raise ValidatorError(f"Actual: {actual} is not {expect}")
        return self

    def assert_object(self, actual: str) -> "ResponseValidator":
        return self.assert_type(actual, dict)

    def assert_array(self, actual: str) -> "ResponseValidator":
        return self.assert_type(actual, list)

    def assert_number(self, actual: str) -> "ResponseValidator":
        return self.assert_type(actual, int)

    def assert_string(self, actual: str) -> "ResponseValidator":
        return self.assert_type(actual, str)

    def assert_boolean(self, actual: bool) -> "ResponseValidator":
        return self.assert_type(actual, bool)

    def assert_null(self, actual: str) -> "ResponseValidator":
        return self.assert_type(actual, type(None))
