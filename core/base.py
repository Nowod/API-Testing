import pytest

from .client import Client


class BaseTestCase:
    @pytest.fixture(scope="session")
    def client(self):
        return Client()
