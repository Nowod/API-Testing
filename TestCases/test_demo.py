"""
测试用例Demo
"""

import json

import pytest
import responses

from core import Client, TestCase


class TestDemo(TestCase):
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
            client.get("http://example.com")
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
            .assert_status_code(200)
            .assert_timing(0.5)
            .assert_header("Content-Type", "application/json")
            .assert_equal("$.Hello", "World")
        )

    @responses.activate
    @pytest.mark.parametrize(
        "req",
        [
            {"xx": "post test"},
            {"xx": "post test", "yy": "post test"},
        ],
    )
    def test_by_parametrize(self, req, client: Client):
        responses.add(
            responses.Response(
                method="POST",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )
        (
            client.post("http://example.com")
            .headers({"Content-Type": "application/json"})
            .body(json.dumps(req))
            .send(timeout=8)
            .assert_status_code(200)
            .assert_timing(0.5)
            .assert_header("Content-Type", "application/json")
            .assert_equal("$.Hello", "World")
        )
