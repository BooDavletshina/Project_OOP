from src.product import Product


class Smartphone(Product):
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии
    efficiency: str  # производительность
    model: str  # модель
    memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод инициализации дочернего класса: Смартфоны"""
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            full_cost_products = self.__price * self.quantity + other.__price * other.quantity
            return f"Полная стоимость всех товаров на складе:{full_cost_products} руб."
        raise TypeError

# if __name__ == "__main__":
#     smartphone_1 = Smartphone("Samsung Galaxy C23 Ultra",
#                               "256GB, Серый цвет, 200MP камера",
#                               180000.0,
#                               5, "8", "C23 Ultra", 256, "серый")
#
#     smartphone_2 = Product("Iphone 15",
#                            "512GB, Gray space",
#                            210000.0,
#                            8)
#
#     smartphone_3 = Smartphone("Samsung Galaxy C23 Ultra",
#                               "256GB, Серый цвет, 200MP камера",
#                               180000.0,
#                               5, "8", "C23 Ultra", 256, "серый")
#
#     print(smartphone_1.name)
#     print(smartphone_1.description)
#     print(smartphone_1.price)
#     print(smartphone_1.quantity)
#
#     print(smartphone_1.efficiency)
#     print(smartphone_1.model)
#     print(smartphone_1.memory)
#     print(smartphone_1.color)
#
#     print(smartphone_1 + smartphone_3)
#     print(smartphone_1 + smartphone_2)
