import unittest
from src.lab1.calculator import calculate

class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(2, 7, "+"), 9)
        self.assertEqual(calculate(-5, 5, "+"), 0)
        self.assertEqual(calculate(2.3, 1.5, "+"), 3.8)
        self.assertEqual(calculate(3.123, 4.545, "+"), 7.668)
        self.assertEqual(calculate("12", "3", "+"), 15)
        self.assertEqual(calculate("-2", 89, "+"), 87)
        self.assertEqual(calculate("6sv", 89, "+"), "Некорректные данные")

    def test_subtraction(self):
        self.assertEqual(calculate(2, 7, "-"), -5)
        self.assertEqual(calculate(-5, 5, "-"), -10)
        self.assertEqual(calculate(2.3, 1.5, "-"), 0.8)
        self.assertEqual(calculate(3.123, 4.545, "-"), -1.422)
        self.assertEqual(calculate("12", "3", "-"), 9)
        self.assertEqual(calculate("-2", 89, "-"), -91)
        self.assertEqual(calculate("6sv", 89, "-"), "Некорректные данные")

    def test_multiplication(self):
        self.assertEqual(calculate(2, 7, "*"), 14)
        self.assertEqual(calculate(-5, 5, "*"), -25)
        self.assertEqual(calculate(2.3, 1.5, "*"), 3.45)
        self.assertEqual(calculate(3.123, 4.545, "*"), 14.19404)
        self.assertEqual(calculate("12", "3", "*"), 36)
        self.assertEqual(calculate("-2", 89, "*"), -178)
        self.assertEqual(calculate("6sv", 89, "*"), "Некорректные данные")

    def test_division(self):
        self.assertEqual(calculate(14, 7, "/"), 2)
        self.assertEqual(calculate(-5, 5, "/"), -1)
        self.assertEqual(calculate(2.505, 0.5, "/"), 5.01)
        self.assertEqual(calculate(5.123, 4.545, "/"), 1.12717)
        self.assertEqual(calculate(45, "0", "/"), "Деление на ноль")
        self.assertEqual(calculate("12", "3", "/"), 4)
        self.assertEqual(calculate("6sv", 89, "/"), "Некорректные данные")
