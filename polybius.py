import string
from ciphers import Cipher


class Polybius(Cipher):
    '''A Polybius Square is a table that allows someone to translate letters
    into numbers. To give a small level of encryption, this table can be
    randomized and shared with the recipient. In order to fit the 26 letters
    of the alphabet into the 25 spots created by the table, the letters i and
    j are usually combined.
    '''

    def __init__(self):
        '''Initializes the new Polybius object'''
        self.alphabet = string.ascii_lowercase
        self.table = []
        for x in range(1, 6):
            for y in range(1, 6):
                self.table.append(str(x) + str(y))
        self.table.insert(8, '24')

    def encrypt(self, message):
        '''Encrypts message to coordinates if Polybius table'''
        output = []
        message = message.lower()
        for letter in message:
            try:
                output.append(self.table[self.alphabet.index(letter)])
            except ValueError:
                output.append(letter)

        return ''.join(output).upper()

    def decrypt(self, message):
        '''Decrypts message to coordinates if Polybius table'''
        output = []
        message_list = message.lower().split()

        for word in message_list:
            for i in range(0, len(word), 2):
                try:
                    combined_letter = word[i] + word[i + 1]
                    output.append(
                        self.alphabet[self.table.index(combined_letter)])
                except ValueError:
                    output.append(message[i])
            output.append(' ')

        return ''.join(output).upper()
