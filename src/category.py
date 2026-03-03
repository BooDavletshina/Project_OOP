class Category:
    name: str  # название
    description: str  # описание
    product: list  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.category_count += 1
        Category.product_count += len(product)
