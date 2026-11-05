import pytest

from src.product import Product


def test_product_init(product, product_data):
    """Проверка корректности инициализации Product"""
    assert product.name == product_data["name"]
    assert product.description == product_data["description"]
    assert product.price == product_data["price"]
    assert product.quantity == product_data["quantity"]


def test_new_product(product_data):
    """Проверка класс-метода new_product"""
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Яблоко"
    assert product.price == 50.0
    assert product.quantity == 10


def test_price_setter_positive(product):
    """Проверка сеттера цены: положительное значение"""
    product.price = 100.0
    assert product.price == 100.0


def test_price_setter_zero(product, capsys):
    """Проверка сеттера цены: нулевое значение"""
    product.price = 0
    assert product.price == 50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_negative(product, capsys):
    """Проверка сеттера цены: отрицательное значение"""
    product.price = -10.0
    assert product.price == 50.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str():
    """Строковое отображение продукта."""
    p = Product("Яблоко", "Свежее", 80, 15)
    assert str(p) == "Яблоко, 80 руб. Остаток: 15 шт."


def test_product_str_with_float_price():
    """Строковое отображение с float-ценой."""
    p = Product("Яблоко", "Свежее", 80.0, 15)
    assert str(p) == "Яблоко, 80 руб. Остаток: 15 шт."


def test_product_add():
    """Сложение продуктов."""
    a = Product("A", "A", 100, 10)
    b = Product("B", "B", 200, 2)
    assert a + b == 1400


def test_product_add_returns_number():
    """Результат сложения — число."""
    a = Product("A", "A", 100, 10)
    b = Product("B", "B", 200, 2)
    assert isinstance(a + b, (int, float))


def test_product_add_with_non_product():
    """Нельзя сложить продукт с числом."""
    a = Product("A", "A", 100, 10)
    with pytest.raises(TypeError):
        a + 5


def test_product_add_with_string():
    """Нельзя сложить продукт со строкой."""
    a = Product("A", "A", 100, 10)
    with pytest.raises(TypeError):
        a + "строка"
