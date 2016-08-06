class ShiftCipher:
    
    @staticmethod
    def _shift(text, amount):
        shifted_text = ""
        for c in text:
            shifted_text += chr(ord(c) + amount)

        return shifted_text

    @staticmethod
    def encrypt(text="", key=0):
        """
        Encrypts the text by shifting each character "up" the alphabet by the amount specified by key.

        :param text: the text to encrypt
        :param key: each alphabet character of text will be shifted up by this amount
        :return: the encrypted message
        """
        return ShiftCipher._shift(text, key)

    @staticmethod
    def decrypt(text="", key=0):
        """
        Decrypts the text by shifting each character "down" the alphabet by the number of letters specified by the key.

        :param text: the text to decrypt
        :param key: each alphabet character of text will be shifted down by this amount
        :return: the decrypted message
        """
        return ShiftCipher._shift(text, -key)