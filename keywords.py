import string

from ciphers import Cipher


class Keyword(Cipher):
    """A keyword cipher is a form of monoalphabetic substitution. A keyword is
    used as the key, and it determines the letter matchings of the cipher
    alphabet to the plain alphabet. Repeats of letters in the word are removed,
    then the cipher alphabet is generated with the keyword matching to A, B, C
    etc. until the keyword is used up, whereupon the rest of the ciphertext
    letters are used in alphabetical order, excluding those already used in the
    key.
    """

    def __init__(self):
        '''Instantiates the object'''
        super().__init__()
        self.alphabet = string.ascii_lowercase
        self.user_key = input('What is your keyword? ').lower()
        self.key = []
        self.output = []

    def remove_nonalpha(self, message):
        new_message = ''
        for letter in message:
            if letter.isalpha() or letter.isspace():
                new_message += letter
        return new_message

    def encrypt(self, message):
        '''Encrypts and returns message'''
        message = self.remove_nonalpha(message.lower())
        for letter in self.user_key:
            if letter in self.alphabet and letter not in self.key:
                self.key.append(letter)
        for letter in self.alphabet:
            if letter not in self.key:
                self.key.append(letter)
        for letter in message:
            if letter == ' ':
                self.output.append(' ')
            else:
                self.output.append(self.key[self.alphabet.index(letter)])
        return ''.join(self.output)

    def decrypt(self, message):
        '''Decrypts and returns message'''
        message = self.remove_nonalpha(message.lower())
        for letter in self.user_key:
            if letter in self.alphabet and letter not in self.key:
                self.key.append(letter)
        for letter in self.alphabet:
            if letter not in self.key:
                self.key.append(letter)
        for letter in message:
            if letter == ' ':
                self.output.append(' ')
            else:
                self.output.append(self.alphabet[self.key.index(letter)])
        return ''.join(self.output)
