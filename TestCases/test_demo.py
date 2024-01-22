"""
传入req
支持 HTTP、HTTP/2 和 WebSocket
req.get(url).assert_equal("actual", "expect")
req.post(url, data).assert_not_equal("actual", "expect")
assert_schema power by pydantic
"""
# import pytest
# from core import Rush
from core.request import Request


class TestDemo:
    """
    测试Demo类
    """

    def test_baidu(self, client: Request):
        res = client.get("https://www.baidu.com").headers({}).send
        assert res.status_code == 200
