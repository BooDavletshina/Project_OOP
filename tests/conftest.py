import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def product_example():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def product_example2():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000,
        quantity=8
    )


@pytest.fixture
def category_example():
    product_1 = Product("Samsung Galaxy C23 Ultra",
                        "256GB, Серый цвет, 200MP камера",
                        180000.0,
                        5)

    product_2 = Product("Iphone 15",
                        "512GB, Gray space",
                        210000.0,
                        8)
    product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[product_1, product_2, product_3]
    )


@pytest.fixture
def product_data_example():
    return {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }


@pytest.fixture
def product_iterator_example(category_example):
    return ProductIterator(category_example)
