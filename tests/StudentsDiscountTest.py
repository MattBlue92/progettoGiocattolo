import unittest
import src.StudentsDiscount as std
import src.Basket as bask

class StudentsDiscountTest(unittest.TestCase):
    def setUp(self):
        self.studentsDiscount=std.StudentsDiscount(0.10)

    def test_apply_discount(self):
        basket=bask.Basket()
        self.assertEqual(10, self.studentsDiscount.applyDiscount(basket))


if __name__ == '__main__':
    unittest.main()
