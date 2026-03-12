from unittest.mock import patch

from src.product import Product


def test_product_init(product_example):
    """Тест на корректность инициализации объектов класса Product"""
    assert product_example.name == "Samsung Galaxy C23 Ultra"
    assert product_example.description == "256GB, Серый цвет, 200MP камера"
    assert product_example.price == 180000.0
    assert product_example.quantity == 5


def test_new_product(product_data_example):
    """Тест на корректное создание объекта класса Product из словаря"""
    new_product = Product.new_product(product_data_example)
    assert new_product.name == "Xiaomi Redmi Note 11"
    assert new_product.description == "1024GB, Синий"
    assert new_product.price == 31000.0
    assert new_product.quantity == 14


def test_price_property(product_example):
    """Тест геттера, который возвращает значение цены товара"""
    assert product_example.price == 180000.0


def test_price_setter(product_example):
    """Тест на повышение цены"""
    product_example.price = 200000.0
    assert product_example.price == 200000.0


def test_price_setter_zero_or_negative(product_example, capsys):
    """Тест на нулевую или отрицательную цену (цена не должна измениться)"""
    product_example.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_example.price == 180000.0

    product_example.price = -500
    assert product_example.price == 180000.0


def test_price_setter_decrease_confirm(product_example):
    """Тест на понижение цены с подтверждением 'y'"""
    with patch('builtins.input', return_value='y'):
        product_example.price = 150000.0

    assert product_example.price == 150000.0


def test_price_setter_decrease_reject(product_example):
    """Тест на понижение цены с отменой 'n'"""
    with patch('builtins.input', return_value='n'):
        product_example.price = 150000.0

    assert product_example.price == 180000.0
