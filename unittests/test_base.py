import responses

from core import ClientType, TestCase


class TestBase(TestCase):
    """
    测试Demo
    """

    @responses.activate
    def test_client(self, client: ClientType):
        responses.add(
            responses.Response(
                method="GET",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )
        (
            client.get("http://example.com")
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
            .assert_status_code(200)
        )
