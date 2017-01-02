#!/usr/bin/env python

import sys

from CryptoAttacks.PublicKey.rsa import RSAKey
from CryptoAttacks.Utils import *

key = RSAKey.import_key("private_key_1024.pem")


def encrypt(message):
    message = b2i(message)
    ciphertext = pow(message, key.e, key.n)
    return i2b(ciphertext)


def parity_oracle(ciphertext):
    ciphertext = b2i(ciphertext)
    message = pow(ciphertext, key.d, key.n)
    if message & 1 == 1:
        return '1'
    return '0'

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ['encrypt', 'decrypt']:
        print "Usage: {} encrypt|decrypt data".format(sys.argv[0])
        sys.exit(1)

    if sys.argv[1] == 'encrypt':
        print encrypt(sys.argv[2].decode('hex')).encode('hex')
    else:
        print parity_oracle(sys.argv[2].decode('hex')).encode('hex')