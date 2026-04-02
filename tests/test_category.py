import pytest

from src.category import Category


def test_category_init(category_example):
    """Тест на корректность инициализации объектов класса Category"""
    assert category_example.name == "Смартфоны"
    assert category_example.description == ("Смартфоны, как средство не только коммуникации, но и получение "
                                            "дополнительных функций для удобства жизни")
    assert len(category_example.product) == 3
    # """Тест на корректный подсчет количества продуктов и подсчет количества категорий"""
    assert category_example.category_count == 1
    assert category_example.product_count == 3


def test_products_property(category_example):
    """Тест на корректность вывода списка товаров в виде строк"""
    assert category_example.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                         "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                         "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")


def test_add_product(category_example, product_example):
    """Тест на корректное добавление продукта в атрибут products"""
    assert len(category_example.product) == 3
    category_example.add_product(product_example)
    assert len(category_example.product) == 3
    assert category_example.product[0].name == "Samsung Galaxy C23 Ultra"
    assert category_example.product[0].quantity == 10


def test_product_property(category_example):
    """Тест геттера, который возвращает значение атрибута products """
    assert len(category_example.product) == 3


def test_category_str(category_example):
    """Тест на корректное выведение строкового отображения"""
    assert str(category_example) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product_error(category_example):
    """Тест на выброс ошибки при добавлении продукта в атрибут products, не относящегося к классу Product"""
    with pytest.raises(TypeError):
        category_example.add_product(1)


def test_add_product_smartphone(category_example, product_smartphone_1):
    """Тест на корректное добавление экземпляра класса Smartphone в атрибут products"""
    category_example.add_product(product_smartphone_1)
    assert category_example.product[0].quantity == 10


def test_middle_price(category_example):
    """Тест на корректный подсчет среднего ценник всех товаров"""
    assert category_example.middle_price() == 140333.33


def test_middle_price_zero_division_error():
    """Тест, на то, что при отсутствии товаров в атрибуте products выведется 0"""
    category_1 = Category("Смартфоны", "Смартфоны", [])
    assert category_1.middle_price() == 0
