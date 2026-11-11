import pytest

from src.smartphone import Smartphone
from src.product import Product


def test_smartphone_init(smartphone):
    """Проверка инициализации смартфона."""
    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == 99.9
    assert smartphone.model == "15 Pro"


def test_smartphone_is_product(smartphone):
    """Смартфон является наследником Product."""
    assert isinstance(smartphone, Product)


def test_smartphone_add(smartphone):
    """Сложение двух смартфонов."""
    phone2 = Smartphone(
        "Samsung", "Хороший", 50000, 2, 98.5, "S23", 128, "Черный"
    )
    assert smartphone + phone2 == 100000 * 5 + 50000 * 2


def test_smartphone_add_with_lawngrass(smartphone):
    """Нельзя сложить смартфон с травой (разные классы)."""
    from src.lawngrass import LawnGrass
    grass = LawnGrass(
        "Трава", "Описание", 500, 10, "Россия", "5 дней", "Зеленый"
    )

    with pytest.raises(TypeError):
        smartphone + grass
