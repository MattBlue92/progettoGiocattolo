import unittest

import src.MumsDiscount as mums
import src.Basket as bask

class TestMumsDiscount(unittest.TestCase):
    def setUp(self):
        self.mumsDiscount=mums.MumsDiscount(0.15)

    def test_apply_discount(self):
        basket=bask.Basket()
        self.assertEqual(15.0, self.mumsDiscount.applyDiscount(basket))


if __name__ == '__main__':
    unittest.main()
