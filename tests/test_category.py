def test_category_init(category_example):
    """Тест на корректность инициализации объектов класса Category"""
    assert category_example.name == "Смартфоны"
    assert category_example.description == ("Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                    "функций для удобства жизни")
    assert category_example.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        }
    ]

    # """Тест на корректный подсчет количества продуктов и подсчет количества категорий"""
    assert category_example.category_count == 1
    assert category_example.product_count == 3
