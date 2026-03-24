import pytest


def test_product_lawn_grass_init(product_lawn_1):
    """Тест на корректную инициализацию экземпляра класса LawnGrass"""
    assert product_lawn_1.name == "Газон синий"
    assert product_lawn_1.description == "Газон синий"
    assert product_lawn_1.price == 180000.0
    assert product_lawn_1.quantity == 5
    assert product_lawn_1.country == "Россия"
    assert product_lawn_1.germination_period == "10 дней"
    assert product_lawn_1.color == "синий"


def test_product_lawn_grass_add(product_lawn_1, product_lawn_2):
    """Тест на сложение двух экземпляров одного и того же класса LawnGrass"""
    assert product_lawn_1 + product_lawn_2 == "Полная стоимость всех товаров на складе:1800000.0 руб."


def test_product_lawn_grass_add_error(product_smartphone_1, product_lawn_1):
    """Тест на выброс ошибки при сложении экземпляров разных классов"""
    with pytest.raises(TypeError):
        _ = product_smartphone_1 + product_lawn_1
