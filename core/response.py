from validator import Validator


class Response:
    def __init__(self, status_code: int, headers: dict, body: dict) -> None:
        self.body = body
        self.status_code = status_code
        self.headers = headers

    def json(self) -> dict:
        return Validator(body=self.body)
