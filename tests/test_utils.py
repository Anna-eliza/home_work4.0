import json

from src.category import Category
from src.utils import load_data_from_json


def test_load_data_from_json(tmp_path):
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Описание смартфонов",
            "products": [
                {
                    "name": "iPhone",
                    "description": "Хороший телефон",
                    "price": 100000.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    file_path = tmp_path / "test_products.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False)

    categories = load_data_from_json(file_path)

    assert isinstance(categories, list)
    assert len(categories) == 1

    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"
    assert "iPhone" in category.products
    assert "100000.0" in category.products

    assert Category.category_count == 1
    assert Category.product_count == 1
