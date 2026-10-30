import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def product_data():
    return {"name": "Яблоко", "description": "Красное",
            "price": 50.0, "quantity": 10}


@pytest.fixture
def product(product_data):
    return Product(**product_data)


@pytest.fixture
def product_list(product):
    return [product, product, product]


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
    yield
