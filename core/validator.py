class Validator:
    def __init__(self, body: str) -> None:
        pass

    def assert_equal(self, actual, expect) -> None:
        assert actual == expect

    def assert_not_equal(self, actual, expect) -> None:
        assert actual != expect
