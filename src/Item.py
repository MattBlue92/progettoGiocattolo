from src.exceptionItem import ExceptionItem


class Item(object):

    def __init__(self, name, price, genre):
        self.name = name
        self.price = price
        self.genre = genre

    def add(self, item):
        if item == None:
            raise TypeError('Input not valid. Please insert an object not null.')
        else:
            raise ExceptionItem("Can't add a Item o Items in an Item")

    def remove(self, item):
        if item == None:
            raise TypeError('Input not valid. Please insert an object not null.')
        else:
            raise ExceptionItem("Can't remove a Item o Items in an Item")

    def getPrice(self):
        return self.price

    def getName(self):
        return self.Name

    def getGenre(self):
        return self.genre

    def getLength(self):
        return 1

    def __str__(self):
        return 'Item(name = '+self.name+', price = '+str(self.price)+'€, genre = '+self.genre+')'








