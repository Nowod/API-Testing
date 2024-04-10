import json

from requests import Response

from core.validator import ResponseValidator


class TestResponseValidator:
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
    validator = ResponseValidator(response, extract={})

    def test_assert_status_code(self):
        self.validator.assert_status_code(200)

    def test_assert_header(self):
        self.validator.assert_header("Content-Type", "application/json")

    def test_assert_timing(self):
        self.validator.assert_timing(0.5)

    def test_assert_exist(self):
        self.validator.assert_exist("$.product.reviews[0].author")

    def test_assert_not_exist(self):
        self.validator.assert_not_exist("$.product.reviews[5].tester")

    def test_assert_equal(self):
        self.validator.assert_equal("$.product.reviews[0].author", "张三")

    def test_assert_not_equal(self):
        self.validator.assert_not_equal("$.product.reviews[0].author", "李四")

    def test_assert_greater_than(self):
        self.validator.assert_greater_than("$.product.reviews[0].rating", 4)

    def test_assert_less_than(self):
        self.validator.assert_less_than("$.product.reviews[0].rating", 6)

    def test_assert_greater_or_equal(self):
        self.validator.assert_greater_or_equal("$.product.reviews[0].rating", 5)

    def test_assert_less_or_equal(self):
        self.validator.assert_less_or_equal("$.product.reviews[0].rating", 5)

    def test_assert_contains(self):
        self.validator.assert_contains(
            "$.product.reviews",
            {
                "author": "张三",
                "date": "2024-03-15T10:00:00Z",
                "rating": 5,
                "review": "手环非常好用，电池续航能力强，监测数据准确。",
            },
        )

    def test_assert_not_contains(self):
        self.validator.assert_not_contains(
            "$.product.reviews",
            {
                "author": "TEST",
                "date": "2024-03-15T10:00:00Z",
                "rating": 5,
                "review": "手环非常好用。",
            },
        )

    def test_assert_in(self):
        self.validator.assert_in("$.product.reviews[0].rating", [4, 5, 6])

    def test_assert_not_in(self):
        self.validator.assert_not_in("$.product.reviews[0].rating", [7, 8])

    def test_assert_schema(self):
        self.validator.assert_schema(
            "$.product.reviews[0]",
            {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "type": "object",
                "properties": {
                    "author": {"type": "string"},
                    "date": {"type": "string"},
                    "rating": {"type": "integer"},
                    "review": {"type": "string"},
                },
                "additionalProperties": False,
                "required": ["author", "date", "rating", "review"],
            },
        )

    def test_assert_pydantic(self):
        from pydantic import BaseModel

        class ProductReview(BaseModel):
            author: str
            date: str
            rating: int
            review: str

        self.validator.assert_pydantic("$.product.reviews[0]", ProductReview)

    def test_assert_regex(self):
        self.validator.assert_regex(
            "$.product.reviews[0].date",
            r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$",
        )

    def test_assert_type(self):
        self.validator.assert_type("$.product.reviews[0].rating", int)

    def test_assert_object(self):
        self.validator.assert_object("$.product")

    def test_assert_array(self):
        self.validator.assert_array("$.product.reviews")

    def test_assert_number(self):
        self.validator.assert_number("$.product.reviews[0].rating")

    def test_assert_string(self):
        self.validator.assert_string("$.product.currency")

    def test_assert_boolean(self):
        self.validator.assert_boolean("$.product.in_stock")

    def test_assert_null(self):
        self.validator.assert_null("$.product.reviews[0].is_null")
