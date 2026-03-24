# from src.category import Category
# from src.product import Product


class ProductIterator:
    def __init__(self, category_obg):
        self.category = category_obg
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.product):
            product = self.category.product[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration

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
#     iterator = ProductIterator(category_1)
#
#     for product in iterator:
#         print(product)
#     print()
#     for product in iterator:
#         print(product)
