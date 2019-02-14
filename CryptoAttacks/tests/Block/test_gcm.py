#!/usr/bin/python

from __future__ import absolute_import, division, print_function

import subprocess
from builtins import bytes, range
from os.path import abspath, dirname
from os.path import join as join_path
from random import randint


from CryptoAttacks.Block.gcm import *
from CryptoAttacks.Utils import log


def test_polynomials():
    print("Test polynomials")
    Pmod = GF_2k_generator(128, [128,7,2,1,0])
    P = Pmod(0b10011010101100110100100110011101100110010111111000111011101000000110110100010101000101100100111100011001010100100110100111011000)
    Q = Pmod(0b01111010101010110111000011011100010011101111000001010000011000010000111010001111100001111010110001001000011101000011111110010101)
    print(P.to_bits(), bin(P.to_int()), P)
    print(Q.to_bits(), bin(Q.to_int()), Q)
    w = P*Q
    print(w.to_bits(), bin(w.to_int()), w)
    assert Q.coefficients == Pmod(Q.coefficients).coefficients
    assert Q.coefficients == Pmod(Q.to_int()).coefficients
    assert Q.coefficients == Pmod(Q.to_bytes()).coefficients
    print('')

    Pmod = GF_2k_generator(10, [11,7,2,1,0])
    c1 = Pmod(1)
    c2 = Pmod(0)
    c3 = Pmod(0)
    c4 = Pmod(0)
    polynomial1 = Polynomial_128([c1,c2,c3,c4])

    c1 = Pmod(1236)
    c2 = Pmod(0)
    c3 = Pmod(0)
    c4 = Pmod(0)
    polynomial2 = Polynomial_128([c1,c2,c3,c4])
    print(polynomial1)
    print(polynomial2)
    print("+", polynomial1 + polynomial2)
    print("*", polynomial1 * polynomial2)
    q = polynomial1 / polynomial2
    r = polynomial1 % polynomial2
    print("/", q)
    print("%", r)
    print('')
    print(polynomial1)
    print(polynomial2*q + r)
    print('')


def test_gcm():
    print("Test GCM")
    plaintext = bytes(b'hn9YA(F BW&B (W&&W(RT&WEF f7*WB FTgsdc')
    additional = bytes(b'j gej8g0SRYH8s  8s9yf sgd78taDS* GASyd ')
    key = bytes(b'xgrtjdh&LA28XNwh')
    nonce = bytes(b'a drO*1@((js')
    ciphertext, tag = gcm_encrypt(plaintext, additional, key, nonce)
    assert gcm_verify(tag, ciphertext, additional, key, nonce)

    blocks = aes_bytes_to_poly_blocks(ciphertext, additional)
    ciphertext2, additional2 = poly_blocks_to_aes_bytes(blocks)
    assert ciphertext == ciphertext2
    assert additional == additional2


def polynomial_factors_product(factorization):
    """factorization: [(poly1, power), (poly2, power)]"""
    result = factorization[0][0].one_element()
    for f, f_degree in factorization:
      result *= f**f_degree
    return result


def test_factor():
    print("Test factor")
    Pmod = GF_2k_generator(9, [9,7,2,1,0])
    c1 = Pmod(31)
    c2 = Pmod(0)
    c3 = Pmod(0)
    c4 = Pmod(3)
    polynomial1 = Polynomial_128([c1,c2,c3,c4])

    c1 = Pmod(237)
    c2 = Pmod(1)
    c3 = Pmod(0)
    c4 = Pmod(10)
    polynomial2 = Polynomial_128([c1,c2,c3,c4])
    polynomial = polynomial1 * polynomial2
    print(polynomial1)
    print(polynomial2)
    print(polynomial)
    print(polynomial.monic())
    print('')

    factorization = factor_polynomial(polynomial)
    print(factorization)
    result = polynomial.one_element()
    for f, f_degree in factorization:
      result *= f**f_degree
    print(result)
    print('')

    assert polynomial_factors_product(factorization) == polynomial.monic()


def test_repeated_nonce():
    print("Test Key-Recovery Attack on GCM with Repeated Nonces")
    for _ in range(3):
        nonce = random_bytes(12)
        key = random_bytes(16)

        h = bytes(AES.new(key, AES.MODE_ECB).encrypt(bytes(b'\x00'*16)))
        h = aes_polynomial(h)
        
        ciphertexts_additionals_tags = []
        for _ in range(4):
            plaintext = random_bytes(randint(0, 50))
            additional = random_bytes(randint(0, 50))
            ciphertext, tag = gcm_encrypt(plaintext, additional, key, nonce)
            ciphertexts_additionals_tags.append((ciphertext, additional, tag))

        valid_ciphertext, valid_additional, valid_tag = ciphertexts_additionals_tags[0]
        auth_key_candidates = recover_key_repated_nonce(ciphertexts_additionals_tags)
        assert h.to_bytes() in auth_key_candidates

        # try found auth key candidates
        correct_auth_key_found = False
        for auth_key in auth_key_candidates:
            forged_ciphertext = random_bytes(randint(0, 10))
            forged_additional = random_bytes(randint(0, 10))
            forged_tag = gcm_forge_tag(ciphertext=forged_ciphertext, additional=forged_additional, auth_key=auth_key,
                valid_ciphertext=valid_ciphertext, valid_additional=valid_additional, valid_tag=valid_tag)

            if gcm_verify(forged_tag, forged_ciphertext, forged_additional, key, nonce):
                correct_auth_key_found = True
                break

        assert correct_auth_key_found


def run():
    log.level = 'debug'

    test_polynomials()
    test_gcm()
    test_factor()
    test_repeated_nonce()


if __name__ == "__main__":
    run()
