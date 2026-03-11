from src.product import Product

class Category:
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    @property
    def products(self):
        """Метод, который позволяет выводить список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity}\n"
        return products_str


    def add_product(self, product: Product):
        """Метод для добавления продукта в атрибут products"""
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy C23 Ultra",
                        "256GB, Серый цвет, 200MP камера",
                        180000.0,
                        5)

    product_2 = Product("Iphone 15",
                        "512GB, Gray space",
                        210000.0,
                        8)

    category_1 = Category("Смартфоны","Смартфоны, как средство", [product_1, product_2])

    print(category_1.products)
    print(category_1.product_count)

    product_3 = Product("Xiaomi Redmi Note 11","1024GB, Синий",31000.0,14)
    category_1.add_product(product_3)
    print(category_1.products)
    print(category_1.product_count)

