from abc import ABC, abstractmethod


class BaseProduct(ABC):  # абстрактный класс(родительский для класса Product

    @abstractmethod
    def __add__(self, other):  # абстрактный метод сложения всех товаров
        pass
