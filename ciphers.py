class Cipher:
    '''Parent class for ciphers'''

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
