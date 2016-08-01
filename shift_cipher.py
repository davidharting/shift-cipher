class ShiftCipher:
    @staticmethod
    def encrypt(text="", key=0):
        """
        Encrypts the text by shifting each character "up" the alphabet by the amount specified by key.

        Inputs
            text: the text to encrypt
            key: each alphabet character of text will be shifted up by this amount
        Outputs
            the encrypted message
        """
        return text;