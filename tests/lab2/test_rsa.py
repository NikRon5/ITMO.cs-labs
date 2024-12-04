import unittest
from src.lab2.rsa import is_prime, gcd,  multiplicative_inverse

class RsaTestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(-10), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(271), True)

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(28, 42), 14)

    def test_multiplicative(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(72, 25), 8)



