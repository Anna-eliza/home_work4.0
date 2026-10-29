import json

from src.category import Category
from src.product import Product
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
        json.dump(
            test_data, f, ensure_ascii=False
        )  # ensure_ascii=False чтобы русские буквы записались нормально

    categories = load_data_from_json(file_path)

    assert isinstance(categories, list)
    assert len(categories) == 1

    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"
    assert len(category.products) == 1

    product = category.products[0]
    assert isinstance(product, Product)
    assert product.name == "iPhone"
    assert product.price == 100000.0

    assert Category.category_count == 1
    assert Category.product_count == 1
