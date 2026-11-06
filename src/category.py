from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: " f"{total_quantity} шт."

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со всеми продуктами (по одному на строке)."""
        if not self.__products:
            return ""
        return "\n".join(str(p) for p in self.__products) + "\n"
