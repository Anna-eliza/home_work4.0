from src.category import Category


def test_category_init(product_list):
    """Проверка корректности инициализации Category"""
    category = Category("Фрукты", "Свежие", product_list)

    assert category.name == "Фрукты"
    assert category.description == "Свежие"

    assert isinstance(category.products, str)
    assert "Яблоко" in category.products
    assert category.products.count("Яблоко") == 3


def test_category_product_count(product_list):
    """Проверка подсчета количества продуктов"""
    Category("Фрукты", "Свежие", product_list)
    assert Category.product_count == 3


def test_category_count(product_list):
    """Проверка подсчета количества категорий"""
    Category("Фрукты", "Свежие", product_list)
    Category("Овощи", "Полезные", product_list)

    assert Category.category_count == 2


def test_add_product(product):
    """Проверка добавления товара через метод add_product"""
    category = Category("Фрукты", "Свежие", [])

    assert Category.product_count == 0
    category.add_product(product)
    assert Category.product_count == 1
    assert "Яблоко" in category.products


def test_add_product_no_return_value(product):
    """Проверка, что add_product ничего не возвращает"""
    category = Category("Фрукты", "Свежие", [])
    result = category.add_product(product)
    assert result is None


def test_products_getter_string_format(product_list):
    """Проверка формата строки, которую возвращает геттер products"""
    category = Category("Фрукты", "Свежие", product_list)
    expected_string = "Яблоко, 50.0 руб. Остаток: 10 шт.\n" * 3
    assert category.products == expected_string
