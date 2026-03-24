import pytest


def test_product_smartphone_init(product_smartphone_1):
    """Тест на корректную инициализацию экземпляра класса Smartphone"""
    assert product_smartphone_1.name == "Samsung Galaxy C23 Ultra"
    assert product_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone_1.price == 180000.0
    assert product_smartphone_1.quantity == 5
    assert product_smartphone_1.efficiency == "8"
    assert product_smartphone_1.model == "C23 Ultra"
    assert product_smartphone_1.memory == 256
    assert product_smartphone_1.color == "серый"


def test_product_smartphone_add(product_smartphone_1, product_smartphone_2):
    """Тест на сложение двух экземпляров одного и того же класса Smartphone"""
    assert product_smartphone_1 + product_smartphone_2 == "Полная стоимость всех товаров на складе:2580000.0 руб."


def test_product_smartphone_add_error(product_smartphone_1, product_example):
    """Тест на выброс ошибки при сложении экземпляров разных классов"""
    with pytest.raises(TypeError):
        _ = product_smartphone_1 + product_example
