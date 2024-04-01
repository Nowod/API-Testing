import pytest

from core.client import Client


@pytest.fixture(scope="session")
def client():
    """请求"""
    return Client()
