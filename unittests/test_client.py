import json

import pytest
import responses
from responses import matchers

from core.client import Client


class TestClient:
    base_url = "http://example.com"

    @responses.activate
    def test_get(self):
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
            .get(self.base_url)
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
            .assert_equal("$.Hello", "World")
            .export("$.Hello", "Hello")
        )

    @responses.activate
    def test_post(self):
        responses.add(
            responses.Response(
                method="POST",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
                match=[matchers.json_params_matcher(json.dumps({"xx": "World"}))],
            ),
        )

        (
            Client()
            ._set_extract({"Hello": "World"})  # test extract
            .post(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "{Hello}"}))
            .send(timeout=8)
            .assert_equal("$.Hello", "World")
        )

    @responses.activate
    def test_put(self):
        responses.add(
            responses.Response(
                method="PUT",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )

        (
            Client()
            .put(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "post"}))
            .send(timeout=8)
            .assert_equal("$.Hello", "World")
        )

    @responses.activate
    def test_patch(self):
        responses.add(
            responses.Response(
                method="PATCH",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )
        (
            Client()
            .patch(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "post"}))
            .send(timeout=8)
            .assert_equal("$.Hello", "World")
        )

    @responses.activate
    def test_delete(self):
        responses.add(
            responses.Response(
                method="DELETE",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )
        (
            Client()
            .delete(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "post"}))
            .send(timeout=8)
            .assert_equal("$.Hello", "World")
        )


if __name__ == "__main__":
    pytest.main(["-s", "test_client.py"])
