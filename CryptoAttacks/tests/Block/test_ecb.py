#!/usr/bin/python

from __future__ import absolute_import, division, print_function

import random
from builtins import range

from Crypto.Cipher import AES, DES3

from CryptoAttacks.Block import ecb
from CryptoAttacks.Utils import add_padding, b2h, log, random_bytes

block_size = AES.block_size
prefix_len = 13
suffix_len = 19
constant = True
key_AES = random_bytes(AES.key_size[-1])
key_DES3 = random_bytes(DES3.key_size[-1])
secret = None


def encryption_oracle_aes(payload):
    global constant, prefix_len, suffix_len, secret
    if secret:
        if constant:
            payload = random_bytes(prefix_len) + payload + secret
        else:
            payload = random_bytes(random.randint(1, 50)) + payload + secret
    else:
        if constant:
            payload = random_bytes(prefix_len) + payload + random_bytes(suffix_len)
        else:
            payload = random_bytes(random.randint(1, 50)) + payload + random_bytes(random.randint(1, 50))

    payload = add_padding(payload, AES.block_size)
    cipher = AES.new(key_AES, AES.MODE_ECB)
    return cipher.encrypt(payload)


def encryption_oracle_des(payload):
    global constant, prefix_len, suffix_len, secret
    if secret:
        if constant:
            payload = random_bytes(prefix_len) + payload + secret
        else:
            payload = random_bytes(random.randint(1, 50)) + payload + secret
    else:
        if constant:
            payload = random_bytes(prefix_len) + payload + random_bytes(suffix_len)
        else:
            payload = random_bytes(random.randint(1, 50)) + payload + random_bytes(random.randint(1, 50))

    payload = add_padding(payload, DES3.block_size)
    cipher = DES3.new(key_DES3, DES3.MODE_ECB)
    return cipher.encrypt(payload)


def test_find_block_size():
    global constant, secret
    print("test: ecb.find_block_size(encryption_oracle, constant=True)")
    secret = None
    constant = True
    for x in range(5):
        guessed_block_size = ecb.find_block_size(encryption_oracle_aes, constant)
        assert guessed_block_size == AES.block_size
        guessed_block_size = ecb.find_block_size(encryption_oracle_des, constant)
        assert guessed_block_size == DES3.block_size

    print("test: ecb.find_block_size(encryption_oracle, constant=False)")
    constant = False
    for x in range(5):
        guessed_block_size = ecb.find_block_size(encryption_oracle_aes, constant)
        assert guessed_block_size == AES.block_size
        guessed_block_size = ecb.find_block_size(encryption_oracle_des, constant)
        assert guessed_block_size == DES3.block_size


def test_find_prefix_suffix_size():
    global constant, prefix_len, suffix_len, secret
    print("test: ecb.find_prefix_suffix_size(encryption_oracle_aes)")
    secret = None
    constant = True
    for x in range(30):
        prefix_len = random.randint(0, 90)
        suffix_len = random.randint(0, 90)
        guessed_ps, guessed_ss = ecb.find_prefix_suffix_size(encryption_oracle_aes, AES.block_size)
        assert prefix_len == guessed_ps and suffix_len == guessed_ss
        guessed_ps, guessed_ss = ecb.find_prefix_suffix_size(encryption_oracle_des, DES3.block_size)
        assert prefix_len == guessed_ps and suffix_len == guessed_ss


def test_decrypt():
    global constant, prefix_len, suffix_len, secret
    print("test: ecb.decrypt(encryption_oracle_aes, constant, block_size=AES.block_size)")
    constant = True
    for x in range(20):
        prefix_len = random.randint(0, 90)
        secret = random_bytes(random.randint(1, 90))
        print("Secret to guess(hex): {}".format(b2h(secret)))
        guessed_secret = ecb.decrypt(encryption_oracle_aes, constant, block_size=AES.block_size)
        assert secret == guessed_secret
        guessed_secret = ecb.decrypt(encryption_oracle_des, constant, block_size=DES3.block_size)
        assert secret == guessed_secret


def run():
    log.level = 'info'
    test_find_block_size()
    test_find_prefix_suffix_size()
    test_decrypt()

if __name__ == "__main__":
    run()
