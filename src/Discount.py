from abc import ABCMeta, abstractmethod


class Discount(metaclass=ABCMeta):
    @abstractmethod
    def applyDiscount(self, basket):
        pass