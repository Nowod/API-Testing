import json
import os
import sys
import unittest

from requests import Response

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)


from core.validator import ResponseValidator  # noqa: E402


class TestResponseValidator(unittest.TestCase):
    def test_assert_equal(self):
        response = Response()
        response.encoding = json.dumps({"Hello": "World"}).encode("utf-8")
        validator = ResponseValidator(response=response)

        validator.assert_equal("$.Hello", {"Hello": "World"})


class TestRequestValidator(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
