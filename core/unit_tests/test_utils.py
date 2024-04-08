import os
import sys
import unittest

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)


from core.utils import extract_json, format_string_by_variable  # noqa: E402


class TestUtils(unittest.TestCase):
    def test_extract_json(self):
        extract_reuslt = extract_json("$.Hello", {"Hello": "World"})
        assert extract_reuslt == "World"

    def test_format_string_by_variable(self):
        format_string = "The Internet has done an {incredible} job of {bringing} the world together in {years} years. "
        variables = {
            "incredible": "incredible",
            "bringing": {"xx": "3424234"},
            "years": 23,
        }
        format_result = format_string_by_variable(format_string, variables)
        assert (
            format_result
            == "The Internet has done an incredible job of {'xx': '3424234'} the world together in 23 years. "
        )


if __name__ == "__main__":
    unittest.main()
