"""
传入req
支持 HTTP、HTTP/2 和 WebSocket
req.get(url).assert_equal("actual", "expect")
req.post(url, data).assert_not_equal("actual", "expect")
assert_schema power by pydantic
"""

import json

from core.client import Client


class TestDemo:
    """
    测试Demo
    """

    base_url = "http://127.0.0.1:8000"

    def test_baidu(self, client: Client):
        client = Client()
        res = (
            client.get(self.base_url)
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
        )
        assert res.status_code == 200
        assert res.headers["Content-Type"] == "application/json"
        assert json.loads(res.text) == {"Hello": "World"}
