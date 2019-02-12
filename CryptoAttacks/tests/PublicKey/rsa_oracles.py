#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

from CryptoAttacks.PublicKey.rsa import RSAKey
from CryptoAttacks.Utils import *


def encrypt(plaintext, key):
    plaintext = b2i(plaintext)
    ciphertext = pow(plaintext, key.e, key.n)
    return i2b(ciphertext)


def decrypt(ciphertext, key):
    ciphertext = b2i(ciphertext)
    plaintext = pow(ciphertext, key.d, key.n)
    return i2b(plaintext)


def sign(message, key):
    # message = add_rsa_signature_padding(message, size=key.size, hash_function='sha1')
    message = b2i(message)
    signature = pow(message, key.d, key.n)
    return i2b(signature)


def verify(message, signature, key):
    # message = add_rsa_signature_padding(message, size=key.size, hash_function='sha1')
    message = b2i(message)
    signature = b2i(signature)
    if pow(signature, key.e, key.n) == message:
        return True
    return False


def parity_oracle(ciphertext):
    key = RSAKey.import_key("private_key_1024.pem")
    ciphertext = b2i(ciphertext)
    message = pow(ciphertext, key.d, key.n)
    if message & 1 == 1:
        return 1
    return 0


def verify_bleichenbacher_suffix(message, signature, key, hash_function='sha1'):
    """00 01 00 ASN1 HASH garbage"""
    hash_asn1 = {
        'md5': '\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
        'sha1': '\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14',
        'sha256': '\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
        'sha384': '\x30\x41\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30',
        'sha512': '\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40'
    }
    hash_msg = getattr(hashlib, hash_function)(message).digest()
    asn1 = hash_asn1[hash_function]
    signature = b2i(signature)

    plain = i2b(key.encrypt(signature), size=1024)
    try:
        plain_hash = plain[plain.index('\x00', 2) + 1:]  # have ASN1 HASH garbage
    except:
        return False
    plain_hash = plain_hash[:len(asn1 + hash_msg)]  # have ANS1 HASH
    if plain[:2] == "\x00\x01" and plain_hash == asn1 + hash_msg:
        return True
    return False


def verify_bleichenbacher_middle(message, signature, key, hash_function='sha1'):
    """00 01 garbage 00 ANS1 HASH"""
    hash_asn1 = {
        'md5': '\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
        'sha1': '\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14',
        'sha256': '\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
        'sha384': '\x30\x41\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30',
        'sha512': '\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40'
    }
    hash_msg = getattr(hashlib, hash_function)(message).digest()
    asn1 = hash_asn1[hash_function]
    signature = b2i(signature)

    plain = i2b(key.encrypt(signature), size=1024)
    try:
        plain_hash = plain[plain.index('\x00', 2) + 1:]  # have ASN1 HASH
    except:
        return False
    if plain[:2] == "\x00\x01" and plain_hash == asn1 + hash_msg:
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) < 4 or sys.argv[1] not in ['encrypt', 'decrypt', 'sign', 'verify', 'parity', 'verify_bleichenbacher_middle', 'verify_bleichenbacher_suffix']:
        print("Usage: {} encrypt|decrypt|sign|verify|parity|verify_bleichenbacher_suffix|verify_bleichenbacher_middle " \
              "key hexdata [more hexdata]".format(sys.argv[0]))
        sys.exit(1)

    key = RSAKey.import_key(sys.argv[2])

    if sys.argv[1] == 'encrypt':
        print(b2h(encrypt(h2b(sys.argv[3]), key)))

    elif sys.argv[1] == 'decrypt':
        print(b2h(decrypt(h2b(sys.argv[3]), key)))

    elif sys.argv[1] == 'sign':
        print(b2h(sign(h2b(sys.argv[3]), key)))

    elif sys.argv[1] == 'verify':
        print(verify(h2b(sys.argv[3]), h2b(sys.argv[4]), key))

    elif sys.argv[1] == 'parity':
        print(parity_oracle(h2b(sys.argv[3])))

    elif sys.argv[1] == 'verify_bleichenbacher_suffix':
        message = h2b(sys.argv[3])
        signature = h2b(sys.argv[4])
        hash_function = sys.argv[5]
        print(verify_bleichenbacher_suffix(message, signature, key, hash_function))

    elif sys.argv[1] == 'verify_bleichenbacher_middle':
        message = h2b(sys.argv[3])
        signature = h2b(sys.argv[4])
        hash_function = sys.argv[5]
        print(verify_bleichenbacher_middle(message, signature, key, hash_function))