"""
传入req
支持 HTTP、HTTP/2 和 WebSocket
req.get(url).assert_equal("actual", "expect")
req.post(url, data).assert_not_equal("actual", "expect")
assert_schema power by pydantic
"""

import responses

from core.client import Client


class TestDemo:
    """
    测试Demo
    """

    @responses.activate
    def test_baidu(self, client: Client):
        responses.add(
            responses.Response(
                method="GET",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )
        (
            Client()
            .get("http://example.com")
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
            .assert_status_code(200)
            .assert_header("Content-Type", "application/json")
            .assert_equal("$.Hello", "World")
        )
