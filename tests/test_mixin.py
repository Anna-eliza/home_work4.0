from src.product import Product


def test_mixin_prints_on_init(capsys):
    Product("Яблоко", "Красное", 50.0, 10)
    captured = capsys.readouterr()
    assert "Product" in captured.out
    assert "Яблоко" in captured.out
    assert "50.0" in captured.out
    assert "10" in captured.out


def test_mixin_repr_format():

    product = Product("Яблоко", "Красное", 50.0, 10)
    expected_repr = "Product('Яблоко', 'Красное', 50.0, 10)"
    assert repr(product) == expected_repr
