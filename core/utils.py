import json
from typing import Any, Dict, List, Mapping, Union

from jsonpath import jsonpath


def extract_json(jsonpath_expr: str, json_str: Union[str, Dict]) -> Dict:
    json_data = json_str
    if isinstance(json_data, str):
        json_data = json.loads(json_data)
    extract_result = jsonpath(json_data, jsonpath_expr)
    if extract_result:
        return extract_result[0]
    else:
        return None


def format_string_by_variable(format_str: Any, variables: Mapping) -> Any:
    if isinstance(format_str, (str, bytes)):
        tmp = format_str.format(**variables)
        return tmp
    else:
        return format_str


def deep_traverse_and_format(
    data: Union[List, Mapping], variables: Mapping
) -> Union[List, Dict]:
    if isinstance(data, dict):
        # format key
        # for key, value in data.items():
        #     key_formatted = format_string_by_variable(key, variables)
        #     if key != key_formatted:
        #         data.pop(key, None)
        #         data[key_formatted] = value
        # format value
        for key, value in data.items():
            if isinstance(value, (str, bytes)):
                data[key] = format_string_by_variable(value, variables)
            elif isinstance(value, (list, dict)):
                deep_traverse_and_format(value, variables)
    elif isinstance(data, list):
        for index in range(len(data)):
            if isinstance(data[index], str):
                data[index] = format_string_by_variable(data[index], variables)
            elif isinstance(data[index], (list, dict)):
                deep_traverse_and_format(data[index], variables)

    return data
