import pytest


def test_product_iterator(product_iterator_example):
    """"""
    iter(product_iterator_example)
    assert product_iterator_example.index == 0
    assert next(product_iterator_example).name == "Samsung Galaxy C23 Ultra"
    assert next(product_iterator_example).name == "Iphone 15"
    assert next(product_iterator_example).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator_example)
