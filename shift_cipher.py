class ShiftCipher:
    @staticmethod
    def encrypt(text="", key=0):
        """
        Encrypts the text by shifting each character "up" the alphabet by the amount specified by key.

        :param text: the text to encrypt
        :param key: each alphabet character of text will be shifted up by this amount
        :return: the encrypted message
        """
        cipher_text = ""
        for c in text:
            cipher_text += chr(ord(c) + key)

        return cipher_text;

    @staticmethod
    def decrypt(text="", key=0):
        """
        Decrypts the text by shifting each character "down" the alphabet by the number of letters specified by the key.

        :param text: the text to decrypt
        :param key: each alphabet character of text will be shifted down by this amount
        :return: the decrypted message
        """
        return text;