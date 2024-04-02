import json

from jsonpath import jsonpath


def extract_json(jsonpath_expr: str, json_str: str | dict) -> dict:
    json_data = json_str
    if isinstance(json_data, str):
        json_data = json.loads(json_data)
    extract_result = jsonpath(json_data, jsonpath_expr)
    if extract_result:
        return extract_result[0]
    else:
        return None
