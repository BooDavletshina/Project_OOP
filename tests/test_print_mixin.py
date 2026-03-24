from src.product import Product
from src.product_smartphone import Smartphone
from src.product_lawn_grass import LawnGrass


def test_print_mixin(capsys):
    """Тест на вывод информации при создании экземпляра класса"""
    Product("Iphone 15", "512GB, Gray space", 210000, 8)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Iphone 15, 512GB, Gray space, 210000, 8)'

    Smartphone("Samsung Galaxy C23 Ultra",
               "256GB, Серый цвет, 200MP камера",
               180000.0,
               5,
               "8",
               "C23 Ultra",
               256,
               "серый")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)'

    LawnGrass("Газон синий", "Газон синий", 180000.0, 5, "Россия", "10 дней", "синий")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(Газон синий, Газон синий, 180000.0, 5)'
