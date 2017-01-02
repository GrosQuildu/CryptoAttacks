#!/usr/bin/env python

from CryptoAttacks.Hash import *
import hashlib


def test_sha1():
    print "Test: sha1"
    for x in range(30):
        tmp = random_str(random.randint(0, 256))
        assert sha1(tmp) == hashlib.sha1(tmp).digest()


def test_md4():
    print "Test: md4"
    assert md4("") == "31d6cfe0d16ae931b73c59d7e0c089c0".decode('hex')
    assert md4("a") == "bde52cb31de33e46245e05fbdbd6fb24".decode('hex')
    assert md4("abc") == "a448017aaf21d8525fc10ae87aa6729d".decode('hex')
    assert md4("message digest") == "d9130a8164549fe818874806e1c7014b".decode('hex')
    assert md4("abcdefghijklmnopqrstuvwxyz") == "d79e1c308aa5bbcdeea8ed63df412da9".decode('hex')
    assert md4("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") == "043f8582f241db351ce627e153e7f0e4".decode('hex')
    assert md4("12345678901234567890123456789012345678901234567890123456789012345678901234567890") == "e33b4ddc9c38f2199c3e7b164fcc0536".decode('hex')


def test_length_extension():
    print "Test length extension sha1"
    for x in range(30):
        secret = random_str(random.randint(0, 130))
        new_message = random_str(random.randint(0, 130))
        hash = sha1(secret)
        new_hash, new_data = length_extension(hash, new_message, len(secret), type='sha1')
        assert sha1(secret+new_data) == new_hash

    print "Test length extension md4"
    for x in range(30):
        secret = random_str(random.randint(0, 130))
        new_message = random_str(random.randint(0, 130))
        hash = md4(secret)
        new_hash, new_data = length_extension(hash, new_message, len(secret), type='md4')
        assert md4(secret + new_data) == new_hash


test_sha1()
test_md4()
test_length_extension()