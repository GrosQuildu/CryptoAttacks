#!/usr/bin/python

import sys

from Crypto.Cipher import AES
from CryptoAttacks.Utils import *

KEY = 'asdf'*4


def encrypt(data):
    iv = ''.join(random_bytes(AES.block_size))
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    return iv+aes.encrypt(add_padding(data))


def decrypt(data):
    iv = data[:AES.block_size]
    data = data[AES.block_size:]
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    p = aes.decrypt(data)
    try:
        p = strip_padding(p, AES.block_size)
        return p
    except:
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ['encrypt', 'decrypt']:
        print "Usage: {} encrypt|decrypt data".format(sys.argv[0])
        sys.exit(1)
    if sys.argv[1] == 'encrypt':
        print encrypt(sys.argv[2].decode('hex')).encode('hex')
    else:
        print decrypt(sys.argv[2].decode('hex')).encode('hex')