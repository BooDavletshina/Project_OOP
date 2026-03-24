from src.product import Product


class LawnGrass(Product):
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии
    country: str  # страна-производитель
    germination_period: str  # срок прорастания
    color: str  # цвет

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод инициализации дочернего класса: Трава газонная"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            full_cost_products = self.price * self.quantity + other.price * other.quantity
            return f"Полная стоимость всех товаров на складе:{full_cost_products} руб."
        raise TypeError

# if __name__ == "__main__":
#     lawn_1 = LawnGrass("Газон красный", "Газон красный", 180000.0, 5, "Россия", "10 дней", "красный")
#     lawn_2 = LawnGrass("Газон синий", "Газон синий", 180000.0, 5, "Россия", "10 дней", "синий")
#
#     smartphone = Product("Iphone 15",
#                          "512GB, Gray space",
#                          210000.0,
#                          8)
#
#     print(lawn_1.name)
#     print(lawn_1.description)
#     print(lawn_1.price)
#     print(lawn_1.quantity)
#
#     print(lawn_1.country)
#     print(lawn_1.germination_period)
#     print(lawn_1.color)
#
#     print(lawn_1 + lawn_2)
#     print(lawn_1 + smartphone)
