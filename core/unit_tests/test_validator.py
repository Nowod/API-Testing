import os
import sys
import unittest

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

import json

from requests import Request, Response

from core.validator import Validator


class TestClient(unittest.TestCase):
    def test_validator(self):
        request = Request()
        response = Response()
        response.encoding = json.dumps({"Hello": "World"}).encode("utf-8")
        validator = Validator(request=request, response=response)

        validator.assert_equal("$.Hello", {"Hello": "World"})


if __name__ == "__main__":
    unittest.main()
