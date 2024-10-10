import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CaesarTestCase(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt_caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23), "XYZABCDEFGHIJKLMNOPQRSTUVW")
        self.assertEqual(encrypt_caesar("ATTACKATONCE", 4), "EXXEGOEXSRGI")
        self.assertEqual(encrypt_caesar("ZYX", -1), "YXW")
        self.assertEqual(encrypt_caesar("ZYX", -3), "WVU")

    def test_decrypt(self):
        self.assertEqual(decrypt_caesar("XYZABCDEFGHIJKLMNOPQRSTUVW", 23), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual(decrypt_caesar("EXXEGOEXSRGI", 4), "ATTACKATONCE")
        self.assertEqual(decrypt_caesar("YXW", -1), "ZYX")
        self.assertEqual(decrypt_caesar("WVU", -3), "ZYX")



