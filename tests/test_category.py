from src.category import Category


def test_category_init(product_list):
    """Проверка корректности инициализации Category"""
    category = Category("Фрукты", "Свежие", product_list)

    assert category.name == "Фрукты"
    assert category.description == "Свежие"
    assert category.products == product_list
    assert isinstance(category.products, list)


def test_category_product_count(product_list):
    """Проверка подсчета количества продуктов"""
    Category("Фрукты", "Свежие", product_list)
    assert Category.product_count == 3


def test_category_count(product_list):
    """Проверка подсчета количества категорий"""
    Category("Фрукты", "Свежие", product_list)
    Category("Овощи", "Полезные", product_list)

    assert Category.category_count == 2
