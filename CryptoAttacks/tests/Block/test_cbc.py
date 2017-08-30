#!/usr/bin/python

import subprocess

from Crypto.Cipher import AES
from CryptoAttacks.Block import cbc
from CryptoAttacks.Utils import *

block_size = AES.block_size


def padding_oracle(payload, iv):
    payload = iv + payload
    try:
        subprocess.check_output(['python', './cbc_oracles.py', 'decrypt', b2h(payload)], stderr=None)
    except subprocess.CalledProcessError:
        return False
    return True


def decryption_oracle(payload):
    blocks_with_correct_padding = h2b(subprocess.check_output(['python', './cbc_oracles.py', 'encrypt',
                                                               b2h('A' * (AES.block_size + 2))]).strip())[
                                  -2 * AES.block_size:]
    iv = 'A'*AES.block_size
    payload = iv + payload + blocks_with_correct_padding
    plaintext = h2b(subprocess.check_output(['python', './cbc_oracles.py', 'decrypt', b2h(payload)], stderr=None).strip())
    return plaintext[:-(AES.block_size+2)]  # strip 'A'*17


def test_decrypt(from_test=1):
    original_plaintext = "testItLongText siaxlla bam!"
    original_ciphertext = h2b(subprocess.check_output(
        ['python', './cbc_oracles.py', 'encrypt', b2h(original_plaintext)]).strip())
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True)
        assert decrypted == original_plaintext

    if from_test <= 2:
        data = original_ciphertext[:-block_size - 1] + 'A' + original_ciphertext[-block_size:]
        print("Test: cbc.decrypt(data, padding_oracle=padding_oracle, is_correct=False)")
        decrypted = cbc.decrypt(data, padding_oracle=padding_oracle, is_correct=False)
        assert decrypted[-block_size:-1] == original_plaintext[-block_size:-1]

    if from_test <= 3:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=False)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=False)
        assert decrypted[:-1] == original_plaintext[:-1]

    if from_test <= 4:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print("Test: cbc.decrypt(data, padding_oracle=padding_oracle, iv=iv)")
        decrypted = cbc.decrypt(data, padding_oracle=padding_oracle, iv=iv)
        assert decrypted == original_plaintext

    if from_test <= 5:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, amount=2)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, amount=2)
        assert decrypted == original_plaintext[-block_size * 2:]

    if from_test <= 6:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, amount=1, is_correct=True)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, amount=1, is_correct=True)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 7:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True, \n \
                                 known_plaintext=original_plaintext)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True,
                                known_plaintext=original_plaintext)
        assert decrypted == original_plaintext

    if from_test <= 8:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True, \n \
                                 known_plaintext=original_plaintext[-4:])")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True,
                                known_plaintext=original_plaintext[-4:])
        assert decrypted == original_plaintext

    if from_test <= 9:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True, \n \
                                 known_plaintext=original_plaintext[-7:], amount=1)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True,
                                known_plaintext=original_plaintext[-7:], amount=1)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 10:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=False, \n \
                                 known_plaintext=original_plaintext[-7:], amount=1)")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=False,
                                known_plaintext=original_plaintext[-7:], amount=1)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 11:
        print("Test: cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True, \n \
                                 known_plaintext=original_plaintext[-block_size - 3:])")
        decrypted = cbc.decrypt(original_ciphertext, padding_oracle=padding_oracle, is_correct=True,
                                known_plaintext=original_plaintext[-block_size - 3:])
        assert decrypted == original_plaintext

    if from_test <= 12:
        print("Test: cbc.decrypt(original_ciphertext, decryption_oracle=decryption_oracle, is_correct=True, \n \
                                 known_plaintext=original_plaintext[-block_size - 3:])")
        decrypted = cbc.decrypt(original_ciphertext, decryption_oracle=decryption_oracle, is_correct=True,
                                known_plaintext=original_plaintext[-block_size - 3:])
        assert decrypted == original_plaintext


def test_fake_ciphertext_padding_oracle(from_test=1):
    new_plaintext = "Some other text we want to fake due to padding oracle."
    new_plaintext_padded = add_padding(new_plaintext, block_size)
    original_plaintext = "Whatever but length must be similar to new plaintext modulo16"
    original_ciphertext = h2b(subprocess.check_output(
        ['python', './cbc_oracles.py', 'encrypt', b2h(original_plaintext)]).strip())
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 2:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,"
              "original_ciphertext=original_ciphertext)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,
                                             original_ciphertext=original_ciphertext)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 3:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle, \n "
              "original_ciphertext=original_ciphertext, original_plaintext=original_plaintext)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,
                                             original_ciphertext=original_ciphertext, original_plaintext=original_plaintext)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 4:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,"
              "original_ciphertext=original_ciphertext, original_plaintext=original_plaintext[-3:])")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,
                                             original_ciphertext=original_ciphertext,
                                             original_plaintext=original_plaintext[-3:])
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 5:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,"
              "original_ciphertext=data, iv=iv)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, padding_oracle=padding_oracle,
                                             original_ciphertext=data, iv=iv)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext


def test_fake_ciphertext_decryption_oracle(from_test=1):
    new_plaintext = "Some other text we want to fake due to padding oracle."
    new_plaintext_padded = add_padding(new_plaintext, block_size)
    original_plaintext = "Whatever but length must be similar to new plaintext modulo16"
    original_ciphertext = h2b(subprocess.check_output(
        ['python', './cbc_oracles.py', 'encrypt', b2h(original_plaintext)]).strip())
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 2:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle,"
              "original_ciphertext=original_ciphertext)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle,
                                             original_ciphertext=original_ciphertext)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 3:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle, \n"
              "original_ciphertext=original_ciphertext, original_plaintext=original_plaintext)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle,
                                             original_ciphertext=original_ciphertext,
                                             original_plaintext=original_plaintext)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 4:
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle, \n"
              "original_ciphertext=original_ciphertext, original_plaintext=original_plaintext[-3:])")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle,
                                             original_ciphertext=original_ciphertext,
                                             original_plaintext=original_plaintext[-3:])
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext

    if from_test <= 5:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print("Test: cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle,"
              "original_ciphertext=data, iv=iv)")
        new_ciphertext = cbc.fake_ciphertext(new_plaintext_padded, decryption_oracle=decryption_oracle,
                                             original_ciphertext=data, iv=iv)
        decrypted = h2b(subprocess.check_output(
            ['python', './cbc_oracles.py', 'decrypt', b2h(new_ciphertext)]).strip())
        assert decrypted == new_plaintext


def test_bit_flipping():
    print("Test: cbc.bit_flipping(ciphertext=ciphertext[-2*AES.block_size:],"
          "plaintext=add_padding(plaintext)[-AES.block_size:],\nwanted_last_block=wanted, block_size=AES.block_size)")

    plaintext = "money=10000&userdata=whateverdata%20huehuehue%20spam%20and%20eggs"
    wanted = add_padding('&admin=true')
    ciphertext = h2b(subprocess.check_output(['python', './cbc_oracles.py', 'encrypt', b2h(plaintext)]).strip())

    fake_cipher = cbc.bit_flipping(ciphertext=ciphertext[-2*AES.block_size:], plaintext=add_padding(plaintext)[-AES.block_size:],
                                   wanted=wanted, block_size=AES.block_size)
    fake_cipher = ciphertext[-AES.block_size*2:] + fake_cipher
    decrypted = h2b(subprocess.check_output(['python', './cbc_oracles.py', 'decrypt', b2h(fake_cipher)]).strip())
    assert decrypted[-len("&admin=true"):] == "&admin=true"


def run():
    log.level = 'info'
    test_decrypt(1)
    test_fake_ciphertext_padding_oracle(1)
    test_fake_ciphertext_decryption_oracle(1)
    test_bit_flipping()

if __name__ == "__main__":
    run()
