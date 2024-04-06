"""
测试用例Demo
"""

import json

import responses

from core.client import Client


class TestDemo:
    """
    测试Demo
    """

    @responses.activate
    def test_get(self, client: Client):
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
            .assert_timing(0.5)
            .assert_header("Content-Type", "application/json")
            .assert_equal("$.Hello", "World")
        )

    @responses.activate
    def test_post(self, client: Client):
        responses.add(
            responses.Response(
                method="POST",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )
        (
            Client()
            .post("http://example.com")
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "post test"}))
            .send(timeout=8)
            .assert_status_code(200)
            .assert_timing(0.5)
            .assert_header("Content-Type", "application/json")
            .assert_equal("$.Hello", "World")
        )
