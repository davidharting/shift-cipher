class ShiftCipher:
    @staticmethod
    def encrypt(text="", key=0):
        """
        Encrypts the text by shifting each character "up" the alphabet by the amount specified by key.

        :param text: the text to encrypt
        :param key: each alphabet character of text will be shifted up by this amount
        :return: the encrypted message
        """
        return text;