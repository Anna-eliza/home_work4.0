def test_product_init(product, product_data):
    """Проверка корректности инициализации Product"""
    assert product.name == product_data["name"]
    assert product.description == product_data["description"]
    assert product.price == product_data["price"]
    assert product.quantity == product_data["quantity"]
