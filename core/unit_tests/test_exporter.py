import json
import os
import sys
import unittest

from requests import Response

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_path)


from core.exporter import Exporter  # noqa: E402


class TestExporter(unittest.TestCase):
    response = Response()
    response.status_code = 200
    response.headers = {"Content-Type": "application/json"}
    response._content = json.dumps(
        {
            "product": {
                "name": "智能手环",
                "description": "这款智能手环具有健康监测、运动追踪和智能提醒等功能，是您健康管理的好帮手。",
                "price": 199.99,
                "currency": "CNY",
                "in_stock": True,
                "rating": 4.5,
                "is_null": None,
                "reviews": [
                    {
                        "author": "张三",
                        "date": "2024-03-15T10:00:00Z",
                        "rating": 5,
                        "review": "手环非常好用，电池续航能力强，监测数据准确。",
                    },
                    {
                        "author": "李四",
                        "date": "2024-03-20T14:30:00Z",
                        "rating": 4,
                        "review": "设计时尚，功能齐全，但有时候睡眠监测不太准确。",
                    },
                ],
                "seller": {
                    "name": "健康电子专卖店",
                    "location": "中国，北京",
                    "contact": {
                        "phone": "+861391234567",
                        "email": "health_electronics@store.com",
                    },
                    "feedback_score": 98,
                },
            }
        }
    ).encode("utf-8")
    extract = {}
    exporter = Exporter(response, extract)

    def test_export_header(self):
        self.exporter.export("header", "Content-Type", "Content-Type")
        assert self.extract["Content-Type"] == "application/json"

    def test_export_body(self):
        self.exporter.export("$.product.name", "product_name")
        assert self.extract["product_name"] == "智能手环"


if __name__ == "__main__":
    unittest.main()
