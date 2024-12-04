import random
import string
import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class VigenereTestCase(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt_vigenere("GEEKSFORGEEKS", "AYUSH"), "GCYCZFMLYLEIM")
    def test_decrypt(self):
        self.assertEqual(decrypt_vigenere("GCYCZFMLYLEIM", "AYUSH"), "GEEKSFORGEEKS")

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))