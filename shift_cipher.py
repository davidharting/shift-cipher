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
        Encrypts the text by shifting each character "up" (in terms of unicode value) by the amount specified by the key.

        :param text: the text to encrypt
        :param key: each character of text will be shifted up by this amount
        :return: the encrypted message
        """
        return ''.join(ShiftCipher._shift(text, key))

    @staticmethod
    def decrypt(text="", key=0):
        """
        Decrypts the text by shifting each character "down" (in terms of unicode vlaue) by the amount specified by the key.

        :param text: the text to decrypt
        :param key: each character will be shifted down by this amount
        :return: the decrypted message
        """
        return ''.join(ShiftCipher._shift(text, -key))