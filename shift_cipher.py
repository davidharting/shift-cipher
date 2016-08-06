class ShiftCipher:
    
    @staticmethod
    def _shift(text, amount):
        """
        Shift each character in the text by the specified amount. Amount is defined in terms of unicode values. 

        :param text: the text to shift
        :param amont: the amount to shift the text by
        :return: a generator containing the shifted text
        """
        for c in text:
            yield chr(ord(c) + amount)

    @staticmethod
    def encrypt(text="", key=0):
        """
        Encrypts the text by shifting each character "up" the alphabet by the amount specified by key.

        :param text: the text to encrypt
        :param key: each alphabet character of text will be shifted up by this amount
        :return: the encrypted message
        """
        return ''.join(ShiftCipher._shift(text, key))

    @staticmethod
    def decrypt(text="", key=0):
        """
        Decrypts the text by shifting each character "down" the alphabet by the number of letters specified by the key.

        :param text: the text to decrypt
        :param key: each alphabet character of text will be shifted down by this amount
        :return: the decrypted message
        """
        return ''.join(ShiftCipher._shift(text, -key))