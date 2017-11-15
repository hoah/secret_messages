import string
from ciphers import Cipher


class Affine(Cipher):
    """ The affine cipher is a type of monoalphabetic substitution cipher,
    wherein each letter in an alphabet is mapped to its numeric equivalent,
    encrypted using a simple mathematical function, and converted back to a
    letter. The formula used means that each letter encrypts to one other
    letter, and back again, meaning the cipher is essentially a standard
    substitution cipher with a rule governing which letter goes to which. As
    such, it has the weaknesses of all substitution ciphers. Each letter is
    enciphered with the function (ax + b) mod 26, where b is the magnitude of
    the shift.
    """

    def __init__(self):
        """
        Creates instance of the Class Affine using addition modulo 26

        Forumla:
        cipher_index = (alpha * letter_index + beta) % 26
        """
        self.accepted_alpha = [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

        while True:
            try:
                self.alpha = int(input(
                    "Please enter alpha key, " +
                    "should be an odd integer from 3-25, except 13: "))
                if self.alpha in self.accepted_alpha:
                    break
                else:
                    print('Invalid alpha key')
            except ValueError:
                print('Invalid alpha value')

        while True:
            try:
                self.beta = int(input(
                    'Please enter beta key, any integer greater than 1: '))
                if self.beta > 1:
                    break
                else:
                    print('Invalid beta key')
            except ValueError:
                print('Invalide beta key')

        self.alphabet = string.ascii_lowercase
        self.cipher_list = []
        for letter_index in range(26):
            self.cipher_list.append(
                (self.alpha * letter_index + self.beta) % 26)

    def encrypt(self, message):
        '''Encrypts message, requires message to be string'''

        output = []
        message = message.lower()
        for letter in message:
            try:
                output.append(
                    self.alphabet[self.cipher_list[self.alphabet.index(
                        letter)]])
            except ValueError:
                output.append(letter)

        return ''.join(output)

    def decrypt(self, message):
        '''Decrypts message, requires message to be string'''

        output = []
        message = message.lower()
        for letter in message:
            try:
                output.append(
                    self.alphabet[self.cipher_list.index(self.alphabet.index(
                        letter))])
            except ValueError:
                output.append(letter)

        return ''.join(output)
