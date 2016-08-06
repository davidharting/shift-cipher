from shift_cipher import ShiftCipher

def main():
    message = "This is the clear text message full of secrets."
    key = 15
    print(message)

    print("... Encrypting ...")
    encrypted_message = ShiftCipher.encrypt(message, 5)
    print(encrypted_message)

    print("... Decrypting ...")
    decrypted_message = ShiftCipher.decrypt(encrypted_message, 5)
    print(decrypted_message)

if __name__ == "__main__":
    main()
