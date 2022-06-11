import random
from struct import pack, unpack

from utils import *


class RSA(object):
    def __init__(self, size=128):
        self.bit_size = size

        self.__p = generate_large_prime(self.bit_size)
        self.__q = generate_large_prime(self.bit_size)
        while self.__p == self.__q:
            self.__q = generate_large_prime(self.bit_size)

        self.n = self.__p * self.__q
        self.phi = (self.__p - 1) * (self.__q - 1)
        self.__public_key, self.__private_key = self.__generate_keys()

    def __generate_keys(self):
        e = random.randint(2, self.phi - 1)
        while gcd(e, self.phi) != 1:
            e = random.randint(2, self.phi - 1)

        d = inverse(e, self.phi)
        public_key = (e, self.n)
        private_key = (d, self.n)

        return public_key, private_key

    @property
    def public_key(self):
        return self.__public_key
    
    @classmethod
    def process_string(self, message):
        acc = 0
        length = len(message)
        if length % 4:
            extra = (4 - length % 4)
            message = as_bytes('\000') * extra + as_bytes(message)

        for i in range(0, length, 4):
            acc = (acc << 32) + unpack('>I', message[i:i+4])[0]

        return acc

    @classmethod
    def recover_string(self, number):
        s = as_bytes('')
        while number > 0:
            s = pack('>I', number & 0xffffffff) + s
            number = number >> 32
        i = 0
        while i < len(s):
            if s[i] != as_bytes('\000')[0]:
                break
            i += 1
        return s[i:]

    def encrypt(self, message, key):
        self.is_str = 0
        if type(message) is str:
            self.is_str = 1
            message = self.process_string(message)
        e, n = key
        return Ciphertext(exp(message, e, n), self.is_str)

    def decrypt(self, ciphertext):
        d, n = self.__private_key
        if ciphertext.is_str:
            return self.recover_string(exp(ciphertext.text, d, n))
        return exp(ciphertext.text, d, n)

    def sign(self, message):
        self.is_str = 0
        if type(message) is str:
            self.is_str = 1
            message = self.process_string(message)

        d, n = self.__private_key
        return Ciphertext(exp(message, d, n), self.is_str)

    def verify(self, signature, key):
        e, n = key
        if signature.is_str:
            return self.recover_string(exp(signature.text, e, n))
        return exp(signature.text, e, n)

class Ciphertext():
    def __init__(self, text, is_str=0):
        self.text = text
        self.is_str = is_str
