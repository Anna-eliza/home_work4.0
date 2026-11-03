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
