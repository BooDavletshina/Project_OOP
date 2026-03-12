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
    assert category_example.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5\n"
                                         "Iphone 15, 210000.0 руб. Остаток: 8\n"
                                         "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14\n")


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
