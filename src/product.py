from src.baseproduct import BaseProduct
from src.mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return (
            f"{self.name}, {self.price:.0f} руб. "
            f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя сложить {type(self).__name__} "
                f"с {type(other).__name__}"
            )
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(**product_data)
