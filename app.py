from shift_cipher import ShiftCipher

def main():
    message = "This is the raw message full of secrets."
    encrypted_message = ShiftCipher.encrypt(message, 5)
    print(encrypted_message)

if __name__ == "__main__":
    main()
