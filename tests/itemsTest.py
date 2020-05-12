import unittest

from src.Item import Item
from src.Items import Items


class ItemsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.items = Items()

    def testAddWhenInputIsNullShouldRiseException(self):
        with self.assertRaises(TypeError):
            self.items.add(None)

    def testAddWhenInputCorrectShouldIncrease(self):
        item = Item("PC", 2600.0, "Elettronica")
        self.items.add(item)
        self.assertEqual(1,self.items.getLength())

    def testRemoveWhenInputIsNullShouldRiseException(self):
        with self.assertRaises(TypeError):
            self.items.add(None)

    def testRemoveWhenInputCorrectShouldDecrease(self):
        item = Item("PC", 2600.0, "Elettronica")
        self.items.add(item)
        self.items.remove(item)
        self.assertEqual(0,self.items.getLength())

    def testGetPriceWhenZeroItemsInBasketshouldReturnZero(self):
        self.assertEqual(0,self.items.getPrice())

    def testGetPriceWhenZeroItemsInBasketshouldReturnZero(self):
        item1 = Item("PC", 2000.0, "Elettronica")
        item2 = Item("PC1", 4000.0, "Elettronica")
        item3 = Item("PC2", 2000.0, "Elettronica")
        
        self.items.add(item1)
        self.items.add(item2)
        self.items.add(item3)

        self.assertEqual(8000,self.items.getPrice())


if __name__ == '__main__':
    unittest.main()
