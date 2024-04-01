import json
import os
import sys
import unittest

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)

from core.client import Client  # noqa: E402


class TestClient(unittest.TestCase):
    base_url = "http://127.0.0.1:8000"

    def test_get(self):
        client = Client()
        res = (
            client.get(self.base_url)
            .headers({"Content-Type": "application/json"})
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

    def test_post(self):
        client = Client()
        res = (
            client.post(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "post"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

    def test_put(self):
        client = Client()
        res = (
            client.put(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "put"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

    def test_patch(self):
        client = Client()
        res = (
            client.patch(self.base_url)
            .headers({"Content-Type": "application/json"})
            .body(json.dumps({"xx": "patch"}))
            .send(timeout=8)
        )
        self.assertEqual(json.loads(res.text), {"Hello": "World"})

    def test_delete(self):
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
