import json

from src.category import Category
from src.product import Product


def load_data_from_json(file_path):
    categories = []
    with open(file_path, "r", encoding="utf8") as f:
        data = json.load(f)
    for category_dict in data:
        products_list = []

        for product_dict in category_dict["products"]:
            product = Product(
                name=product_dict["name"],
                description=product_dict["description"],
                price=product_dict["price"],
                quantity=product_dict["quantity"],
            )
            products_list.append(product)

        category = Category(
            name=category_dict["name"],
            description=category_dict["description"],
            products=products_list,
        )
        categories.append(category)

    return categories
