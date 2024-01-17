class Response:
    def __init__(self) -> None:
        self.data = None
        self.status_code = None

    def json(self) -> dict:
        return self.data
