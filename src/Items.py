

class Items(object):

    def __init__(self):
        self.basket = []

    def getLength(self):
        len = 0
        for item in self.basket:
            len += item.getLength()
        return len

    def add(self, items):
        if items == None:
            raise TypeError('Input not valid. Please insert an object not null.')
        self.basket.append(items)

    def remove(self, items):
        if items == None:
            raise TypeError('Input not valid. Please insert an object not null.')
        self.basket.remove(items)

    def getPrice(self):
        price = 0
        for item in self.basket:
            price += item.getPrice()
        return price