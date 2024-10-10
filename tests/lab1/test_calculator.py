import unittest
from src.lab1.calculator import addition

class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 7), 9)
        self.assertEqual(addition(-5, 5), 0)
        self.assertEqual(addition(2.3, 1.5), 3.8)
        self.assertEqual(addition(3.123, 4.545), 7.668)
        self.assertEqual(addition("12", "3"), 15)
        self.assertEqual(addition("-2", 89), 87)
        self.assertEqual(addition("6sv", 89), "Некорректные данные")