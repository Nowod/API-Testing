import pytest

from .client import Client


class TestCase:
    @pytest.fixture(scope="session")
    def client(self) -> Client:
        return Client()
