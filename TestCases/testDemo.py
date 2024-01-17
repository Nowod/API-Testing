"""
传入req
支持 HTTP、HTTP/2 和 WebSocket
req.get(url).assert_equal("actual", "expect")
req.post(url, data).assert_not_equal("actual", "expect")
assert_schema power by pydantic
"""
import pytest
from core import Rush


class testDemo(Rush):
    """
    测试Demo类
    """

    def test_baidu(self):
        pytest.skip("跳过")
