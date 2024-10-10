import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class VigenereTestCase(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt_vigenere("GEEKSFORGEEKS", "AYUSH"), "GCYCZFMLYLEIM")
    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere("GCYCZFMLYLEIM", "AYUSH"), "GEEKSFORGEEKS")