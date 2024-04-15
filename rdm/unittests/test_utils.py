from rdm.utils import (  # noqa: E402
    deep_traverse_and_format,
    extract_json,
    format_string_by_variable,
)


class TestUtils:
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

    def test_deep_traverse_and_format(self):
        data = {
            "xx": "The Internet has done an {incredible} job of {bringing} the world together in {years} years. ",
            "{yy}": "post test",
            "zz": ["11", "{num}"],
            "a": {"c": "{b}"},
        }
        variables = {
            "incredible": "incredible",
            "bringing": {"xx": "3424234"},
            "years": 23,
            "num": 11,
            "b": "xxxxx",
            "yy": "yyyyy",
        }
        data = deep_traverse_and_format(data, variables)
        assert data == {
            "xx": "The Internet has done an incredible job of {'xx': '3424234'} the world together in 23 years. ",
            "{yy}": "post test",
            "zz": ["11", "11"],
            "a": {"c": "xxxxx"},
        }
