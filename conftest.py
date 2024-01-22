import pytest
from core.request import Request


@pytest.fixture(scope="session")
def client():
    """请求"""
    return Request()
