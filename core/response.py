from .validator import Validator


class Response:
    def __init__(self, res) -> None:
        self.body = res.text
        self.status_code = res.status_code
        self.headers = res.headers

    def json(self) -> dict:
        return Validator(body=self.body)
