class Product:
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Метод, который принимает параметры товара в словаре и возвращает объект класса Product"""
        return cls(**product_data)

    @property
    def price(self):
        """Геттер, который возвращает значение цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод, который позволяет изменить цену товара"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            user_input = input("Цена понижается. Введите 'y' для подтверждения или 'n' для отмены: ").lower()
            if user_input == 'y':
                self.__price = new_price
                print("Цена успешно понижена")
            else:
                print("Действие отменено, цена осталась прежней")
        else:
            self.__price = new_price

if __name__ == "__main__":
    product_1 = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    product = Product.new_product(product_1) # проверка класс-метода
    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

    product.price = 0
    # product.price = 30000
    product.price = 33000
    print(product.price)
