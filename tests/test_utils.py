from unittest.mock import patch, mock_open

from src.category import Category
from src.utils import read_json, create_object_from_json


def test_read_json():
    """Тест на корректность считывания JSON-файла."""
    mock_data = '{"key": "value"}'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json("fake_path.json")
        assert result == {"key": "value"}


def test_create_object_from_json():
    """Тест на корректно преобразование списка словарей в объекты классов Category и Product."""
    raw_data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [
                {
                    "name": "Iphone",
                    "description": "512GB",
                    "price": 100000.0,
                    "quantity": 10
                }
            ]
        }
    ]

    # Сбрасываем счетчики классов перед тестом
    Category.category_count = 0
    Category.product_count = 0

    result = create_object_from_json(raw_data)

    assert len(result) == 1
    assert isinstance(result[0], Category)
    assert result[0].name == "Смартфоны"
