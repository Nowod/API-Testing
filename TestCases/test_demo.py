"""
传入req
支持 HTTP、HTTP/2 和 WebSocket
req.get(url).assert_equal("actual", "expect")
req.post(url, data).assert_not_equal("actual", "expect")
assert_schema power by pydantic
"""

from lib.client import Client


class TestDemo:
    """
    测试Demo
    """

    def test_baidu(self, client: Client):
        res = client.get("https://www.baidu.com").headers({}).send()
        assert res.status_code == 200
