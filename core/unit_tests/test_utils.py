import os
import sys
import unittest

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)


from core.utils import extract_json  # noqa: E402


class TestUtils(unittest.TestCase):
    def test_extract_json(self):
        extract_reuslt = extract_json("$.Hello", {"Hello": "World"})
        assert extract_reuslt == "World"


if __name__ == "__main__":
    unittest.main()
