import unittest
from shift_cipher import ShiftCipher # unit under test

class ShiftCipherTest(unittest.TestCase):
    def test_encrypt(self):
        cipher_text = ShiftCipher.encrypt("abc", 3)
        self.assertEqual("def", cipher_text)

    def test_decrypt(self):
        clear_text = ShiftCipher.decrypt("def", 3)
        self.assertEqual("abc", clear_text)
        
if __name__ == '__main__':
    unittest.main()