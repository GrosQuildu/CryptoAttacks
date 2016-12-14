#!/usr/bin/python

from Utils import *
from Crypto.Cipher import AES
import sys

KEY = 'asdf'*4


def encrypt(data):
    iv = ''.join(random_byte() for x in xrange(AES.block_size))
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
    if len(sys.argv) != 3:
        print "Usage: ./padding_oracle.py encrypt|decrypt data"
        sys.exit(1)
    if sys.argv[1] == 'encrypt':
        print encrypt(sys.argv[2].decode('hex')).encode('hex')
    else:
        print decrypt(sys.argv[2].decode('hex')).encode('hex')