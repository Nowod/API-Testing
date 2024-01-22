from .validator import Validator


class Response:
    def __init__(self, res_object) -> None:
        self.body = res_object.text
        self.status_code = res_object.status_code
        self.headers = res_object.headers

    def json(self) -> dict:
        return Validator(body=self.body)
