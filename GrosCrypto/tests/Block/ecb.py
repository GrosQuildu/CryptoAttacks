#!/usr/bin/python

from Crypto.Cipher import AES, DES3
from GrosCrypto.Block import ecb
from GrosCrypto.Utils import *

log.level = 'debug'
block_size = AES.block_size
prefix_len = 13
suffix_len = 19
constant = True
key_AES = random_str(AES.key_size[-1])
key_DES3 = random_str(DES3.key_size[-1])
secret = None


def encryption_oracle_aes(payload):
    global constant, prefix_len, suffix_len, secret
    if secret:
        if constant:
            payload = random_str(prefix_len) + payload + secret
        else:
            payload = random_str(random.randint(1, 50)) + payload + secret
    else:
        if constant:
            payload = random_str(prefix_len) + payload + random_str(suffix_len)
        else:
            payload = random_str(random.randint(1, 50)) + payload + random_str(random.randint(1, 50))

    payload = add_padding(payload, AES.block_size)
    cipher = AES.new(key_AES, AES.MODE_ECB)
    return cipher.encrypt(payload)


def encryption_oracle_des(payload):
    global constant, prefix_len, suffix_len, secret
    if secret:
        if constant:
            payload = random_str(prefix_len) + payload + secret
        else:
            payload = random_str(random.randint(1, 50)) + payload + secret
    else:
        if constant:
            payload = random_str(prefix_len) + payload + random_str(suffix_len)
        else:
            payload = random_str(random.randint(1, 50)) + payload + random_str(random.randint(1, 50))

    payload = add_padding(payload, DES3.block_size)
    cipher = DES3.new(key_DES3, DES3.MODE_ECB)
    return cipher.encrypt(payload)


def test_find_block_size():
    global constant, secret
    print "test: ecb.find_block_size(encryption_oracle, constant=True)"
    secret = None
    constant = True
    for x in xrange(5):
        guessed_block_size = ecb.find_block_size(encryption_oracle_aes, constant)
        assert guessed_block_size == AES.block_size
        guessed_block_size = ecb.find_block_size(encryption_oracle_des, constant)
        assert guessed_block_size == DES3.block_size

    print "test: ecb.find_block_size(encryption_oracle, constant=False)"
    constant = False
    for x in xrange(5):
        guessed_block_size = ecb.find_block_size(encryption_oracle_aes, constant)
        assert guessed_block_size == AES.block_size
        guessed_block_size = ecb.find_block_size(encryption_oracle_des, constant)
        assert guessed_block_size == DES3.block_size


def test_find_prefix_suffix_size():
    global constant, prefix_len, suffix_len, secret
    print "test: ecb.find_prefix_suffix_size(encryption_oracle_aes)"
    secret = None
    constant = True
    for x in xrange(5):
        prefix_len = random.randint(0, 50)
        suffix_len = random.randint(0, 50)
        guessed_ps, guessed_ss = ecb.find_prefix_suffix_size(encryption_oracle_aes)
        assert prefix_len == guessed_ps and suffix_len == guessed_ss
        guessed_ps, guessed_ss = ecb.find_prefix_suffix_size(encryption_oracle_des)
        assert prefix_len == guessed_ps and suffix_len == guessed_ss


def test_decrypt():
    global constant, prefix_len, suffix_len, secret
    print "test: ecb.decrypt(encryption_oracle_aes, constant, block_size=AES.block_size)"
    constant = True
    for x in xrange(5):
        prefix_len = random.randint(0, 50)
        secret = random_str(random.randint(0, 50))
        guessed_secret = ecb.decrypt(encryption_oracle_aes, constant, block_size=AES.block_size)
        assert secret == guessed_secret
        guessed_secret = ecb.decrypt(encryption_oracle_des, constant, block_size=DES3.block_size)
        assert secret == guessed_secret

test_find_block_size()
test_find_prefix_suffix_size()
test_decrypt()
