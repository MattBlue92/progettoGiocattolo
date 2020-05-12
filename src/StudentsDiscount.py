from src.Discount import Discount

class StudentsDiscount(Discount):
    def __init__(self, discount):
        self.discount=discount

    def applyDiscount(self, basket):
        return self.discount*basket.getPrice()