#!/usr/bin/python

import sys

from Crypto.Cipher import AES
from GrosCrypto.Utils import *

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
    if check_padding(p):
        return p[:-ord(p[-1])]
    else:
        sys.exit(1)


def check_padding(data):
    padding = data[-1]
    if data[-ord(padding):] == padding*ord(padding):
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ['encrypt', 'decrypt']:
        print "Usage: {} encrypt|decrypt data".format(sys.argv[0])
        sys.exit(1)
    if sys.argv[1] == 'encrypt':
        print encrypt(sys.argv[2].decode('hex')).encode('hex')
    else:
        print decrypt(sys.argv[2].decode('hex')).encode('hex')