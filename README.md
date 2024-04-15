# Redemption
接口自动化测试框架实现，基于Pytest+Requests


## Features

- [x] 链式调用
- [x] 高级assert方法
- [x] response变量提取与使用
- [ ] 协议扩展
- [ ] 用例自动生成

## Installation
```shell
export PYTHONPATH=$PYTHONPATH:/workspaces/Redemption
pip install poetry # Python >= 3.10
poetry install
```

## Demo
TestCases/test_demo.py
```python
import json

import pytest
import responses

from core import ClientType, TestCase


class TestDemo(TestCase):
    """
    testcase demo
    """

    @responses.activate
    def test_get(self, client: ClientType):
        # mock response
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
            .export("body", "$.Hello", "Hello")
        )

    @responses.activate
    @pytest.mark.parametrize(
        "req",
        [
            {"xx": "post {Hello}"},
            {"xx": "post test", "yy": "post test"},
        ],
    )
    def test_by_parametrize(self, req, client: ClientType):
        # mock response
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

```

