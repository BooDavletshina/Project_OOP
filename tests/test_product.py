def test_product_init(product_example):
    """Тест на корректность инициализации объектов класса Product"""
    assert product_example.name == "Samsung Galaxy C23 Ultra"
    assert product_example.description == "256GB, Серый цвет, 200MP камера"
    assert product_example.price == 180000.0
    assert product_example.quantity == 5
