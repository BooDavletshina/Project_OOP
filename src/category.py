from src.product import Product


class Category:
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    category_count = 0  # количество категорий
    product_count = 0  # количество товаров в категории

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        full_product_count = 0
        for product in self.__products:
            full_product_count += product.quantity
        return f"{self.name}, количество продуктов: {full_product_count} шт."

    @property
    def products(self):
        """Метод, который позволяет выводить список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт."""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, new_product: Product):
        """Метод для добавления продукта в атрибут products"""
        if isinstance(new_product, Product):
            for product in self.__products:
                if product.name == new_product.name:  # проверяем на дубликат по имени
                    product.quantity += new_product.quantity  # если дубликат по имени складываем кол-во
                    product.price = max(product.price, new_product.price)  # выбираем максимальную цену
                    break

            else:
                self.__products.append(new_product)
                Category.product_count += 1
        else:
            raise TypeError

    @property
    def product(self):
        """Метод, который возвращает значение атрибута products"""
        return self.__products

    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров"""
        try:
            middle_price = sum([product.price for product in self.__products]) / len(self.__products)
            return round(middle_price, 2)
        except ZeroDivisionError:
            return 0

# if __name__ == "__main__":
#     product_1 = Product("Samsung Galaxy C23 Ultra",
#                         "256GB, Серый цвет, 200MP камера",
#                         180000.0,
#                         5)
#
#     product_2 = Product("Iphone 15",
#                         "512GB, Gray space",
#                         210000.0,
#                         8)
#
#     category_1 = Category("Смартфоны", "Смартфоны, как средство", [product_1, product_2])
#
#     print(category_1.products)
#     print(category_1.product_count)
#
#     product_3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     category_1.add_product(product_3)
#     print(category_1.products)
#     print(category_1.product_count)
#
#     product_4 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 33000.0, 15)
#     category_1.add_product(product_4)
#     print(category_1.products)
#     print(category_1.product_count)
#
#     print(str(category_1))
#     lawn_1 = LawnGrass("Газон красный", "Газон красный", 180000.0, 5, "Россия", "10 дней", "красный")
#     category_1.add_product(lawn_1)
#     print(category_1.products)
