import json
import os
import sys
import unittest

import responses

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

from core.client import Client  # noqa: E402


class TestClient(unittest.TestCase):
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

        client = Client()
        res = (
            client.get(self.base_url)
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

    @responses.activate
    def test_post(self):
        responses.add(
            responses.Response(
                method="POST",
                url="http://example.com",
                headers={"Content-Type": "application/json"},
                json={"Hello": "World"},
            ),
        )

        client = Client()
        res = (
            client.post(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "post"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

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

        client = Client()
        res = (
            client.put(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "put"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

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
        client = Client()
        res = (
            client.patch(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "patch"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

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
        client = Client()
        res = (
            client.delete(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "Wordeleteld"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})


if __name__ == "__main__":
    unittest.main()
