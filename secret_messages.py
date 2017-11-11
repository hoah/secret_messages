from caesar import Caesar


def display_menu():
    menu = '''These are the current available ciphers:

-Caesar
-Atbash
-Transposition
-Keyword
'''
    print(menu)


def validate_cipher_choice():
    cipher_list = ['caesar', 'atbash', 'transposition', 'keyword']
    cipher_choice = ''
    while cipher_choice not in cipher_list:
        cipher_choice = input('Which cipher would you like to use? ').lower()
        # validate choice from available
        if cipher_choice in cipher_list:
            return cipher_choice
        print("We don't have that cipher...")
        display_menu()


def validate_encode_choice():
    choice_list = ['encrypt', 'decrypt']
    encode_choice = ''
    while encode_choice not in choice_list:
        encode_choice = input('Are we going to encrypt or decrypt? ').lower()
        if encode_choice in choice_list:
            return encode_choice


def run_cipher(cipher_choice, message, encode_choice):
    if cipher_choice == 'caesar':
        if encode_choice == 'encrypt':
            return Caesar().encrypt(message)
        elif encode_choice == 'decrypt':
            return Caesar().decrypt(message)


def get_choices():
    display_menu()
    cipher_choice = validate_cipher_choice()
    message = input("That's an excellent cipher. What's the message? ")
    encode_choice = validate_encode_choice()
    message_code = run_cipher(cipher_choice, message, encode_choice)
    print(message_code)


if __name__ == '__main__':
    get_choices()
