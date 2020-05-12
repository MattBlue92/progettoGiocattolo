import unittest

from src.Item import Item
from src.exceptionItem import ExceptionItem


class itemTest(unittest.TestCase):

    def setUp(self) -> None:
        self.item = Item("PC", 2000.0, "Elettronica")


    def testAddWhenInputIsNullShouldRiseException(self):
        with self.assertRaises(TypeError):
            self.item.add(None)

    def testAddWhenInputIsNotNullShouldRiseException(self):
        itemX = Item("PC", 2600.0, "Elettronica")
        with self.assertRaises(ExceptionItem):
            self.item.add(itemX)

    def testRemoveWhenInputIsNullShouldRiseException(self):
        with self.assertRaises(TypeError):
            self.item.remove(None)

    def testRemoveWhenInputIsNotNullShouldRiseException(self):
        itemX = Item("PC", 3600.0, "Elettronica")
        with self.assertRaises(ExceptionItem):
            self.item.remove(itemX)


if __name__ == '__main__':
    unittest.main()
