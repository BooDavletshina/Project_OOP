import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция, которая считывает json-файл"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_object_from_json(data):
    """Функция, которая создает объекты классов."""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    data_dict = read_json("../data/products.json")
    print(data_dict)
    print(create_object_from_json(data_dict))
