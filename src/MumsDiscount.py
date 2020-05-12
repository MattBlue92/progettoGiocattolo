class MumsDiscount:
    def __init__(self, discount):
        self.discount=discount

    def applyDiscount(self, basket):
        return self.discount*basket.getPrice()
