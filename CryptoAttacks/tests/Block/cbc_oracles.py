#!/usr/bin/python

import sys

from Crypto.Cipher import AES
from CryptoAttacks.Utils import *


KEY = 'asdf'*4
iv_as_key = False
block_size = AES.block_size


class BadPadding(RuntimeError):
    pass


def encrypt(data, iv_as_key=False):
    iv = ''.join(random_bytes(block_size))
    if iv_as_key:
        iv = KEY
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    return iv+aes.encrypt(add_padding(data))


def decrypt(data, iv_as_key=False):
    if iv_as_key:
        iv = KEY
    else:
        iv = data[:block_size]
        data = data[block_size:]
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    p = aes.decrypt(data)
    try:
        p = strip_padding(p, block_size)
        return p
    except:
        raise BadPadding


def padding_oracle(payload, iv):
    global iv_as_key
    payload = iv + payload
    try:
        decrypt(payload, iv_as_key)
    except BadPadding:
        return False
    return True


blocks_with_correct_padding = encrypt('A' * (block_size + 5))[block_size:]
def decryption_oracle(payload):
    global iv_as_key
    iv = 'A' * block_size
    payload = iv + payload + blocks_with_correct_padding
    plaintext = decrypt(payload, iv_as_key)
    if iv_as_key:
        return xor(plaintext[block_size:block_size*2], iv)
    return xor(plaintext[:block_size], iv)


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ['encrypt', 'decrypt']:
        print("Usage: {} encrypt|decrypt data".format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[1] == 'encrypt':
        print(b2h(encrypt(h2b(sys.argv[2]))))
    else:
        print(b2h(decrypt(h2b(sys.argv[2]))))