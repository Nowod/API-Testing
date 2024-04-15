import pytest

from .client import Client


class TestCase:
    @pytest.fixture(scope="class")
    def client(self) -> Client:
        return Client()
