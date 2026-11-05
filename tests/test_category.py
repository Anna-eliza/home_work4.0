from src.category import Category
from src.product import Product


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
    category = Category("Фрукты", "Свежие", product_list)
    expected_string = "Яблоко, 50 руб. Остаток: 10 шт.\n" * 3
    assert category.products == expected_string


def test_category_str():
    """Строковое отображение категории."""
    p1 = Product("A", "A", 100, 10)
    p2 = Product("B", "B", 200, 2)
    category = Category("Фрукты", "Свежие", [p1, p2])
    assert str(category) == "Фрукты, количество продуктов: 12 шт."


def test_category_str_empty():
    """Пустая категория."""
    category = Category("Пусто", "Пустая", [])
    assert str(category) == "Пусто, количество продуктов: 0 шт."


def test_category_products_getter():
    p1 = Product("A", "A", 100, 10)
    category = Category("Фрукты", "Свежие", [p1])
    assert category.products == "A, 100 руб. Остаток: 10 шт.\n"
