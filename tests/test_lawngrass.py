import pytest

from src.lawngrass import LawnGrass
from src.product import Product


@pytest.fixture
def lawngrass():
    return LawnGrass(
        name="Газонная трава",
        description="Зеленая и мягкая",
        price=500.0,
        quantity=100,
        country="Россия",
        germination_period="5 дней",
        color="Зеленый"
    )


def test_lawngrass_init(lawngrass):
    """Проверка инициализации травы."""
    assert lawngrass.name == "Газонная трава"
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "5 дней"
    assert lawngrass.color == "Зеленый"


def test_lawngrass_is_product(lawngrass):
    """Трава является наследником Product."""
    assert isinstance(lawngrass, Product)


def test_lawngrass_add(lawngrass):
    """Сложение двух трав."""
    grass2 = LawnGrass(
        "Трава 2", "Описание", 200, 10, "Китай", "3 дня", "Синий"
    )
    assert lawngrass + grass2 == 500 * 100 + 200 * 10


def test_lawngrass_add_with_product():
    """Нельзя сложить траву с базовым продуктом (разные классы)."""
    grass = LawnGrass(
        "Трава", "Описание", 500, 10, "Россия", "5 дней", "Зеленый"
    )
    product = Product(
        "Яблоко", "Красное", 50, 10
    )

    with pytest.raises(TypeError):
        grass + product
