import unittest
import src.StudentsDiscount as std

class StudentsDiscountTest(unittest.TestCase):
    def setUp(self):
        self.studentsDiscount=std.StudentsDiscount()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
