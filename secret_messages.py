import os
from caesar import Caesar
from keywords import Keyword
from affine import Affine
from polybius import Polybius


def clear():
    '''Clears console.'''
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    '''Displays the ciper options'''
    menu = '''These are the current available ciphers:
-Affine
-Caesar
-Keyword
-Polybius
'''
    print(menu)


def validate_cipher_choice():
    """Validates the user's cipher choice against the available ciphers"""
    cipher_list = ['affine', 'caesar', 'keyword', 'polybius']
    cipher_choice = ''
    while cipher_choice not in cipher_list:
        cipher_choice = input('Which cipher would you like to use? ').lower()
        # validate choice from available
        if cipher_choice in cipher_list:
            return cipher_choice
        print("We don't have that cipher...")
        display_menu()


def validate_encode_choice():
    """Validates if the user entered encrypt or decrypt"""
    choice_list = ['encrypt', 'decrypt']
    encode_choice = ''
    while encode_choice not in choice_list:
        encode_choice = input('Are we going to encrypt or decrypt? ').lower()
        if encode_choice in choice_list:
            return encode_choice


def run_cipher(cipher_choice, message, encode_choice):
    '''Executes the chosen cipher'''
    if cipher_choice == 'caesar':
        if encode_choice == 'encrypt':
            return Caesar().encrypt(message)
        elif encode_choice == 'decrypt':
            return Caesar().decrypt(message)
    elif cipher_choice == 'keyword':
        if encode_choice == 'encrypt':
            return Keyword().encrypt(message)
        elif encode_choice == 'decrypt':
            return Keyword().decrypt(message)
    elif cipher_choice == 'affine':
        if encode_choice == 'encrypt':
            return Affine().encrypt(message)
        elif encode_choice == 'decrypt':
            return Affine().decrypt(message)
    elif cipher_choice == 'polybius':
        if encode_choice == 'encrypt':
            return Polybius().encrypt(message)
        elif encode_choice == 'decrypt':
            return Polybius().decrypt(message)


def get_choices():
    '''Runs the sequence for nice display'''
    clear()
    display_menu()
    cipher_choice = validate_cipher_choice()
    clear()
    message = input(
        "{} is an excellent cipher. What's the message? ".format(cipher_choice.capitalize()))
    encode_choice = validate_encode_choice()
    message_code = run_cipher(cipher_choice, message, encode_choice)
    print(message_code)


if __name__ == '__main__':
    while True:
        get_choices()
        run_again = input('Encrypt/Decrypt something else? Y/n ').lower()
        if run_again != 'y':
            break
