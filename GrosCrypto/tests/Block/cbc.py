#!/usr/bin/python

import subprocess

from Crypto.Cipher import AES
from GrosCrypto.Block import cbc
from GrosCrypto.Utils import *

log.level = 'info'
block_size = AES.block_size


def oracle(payload, iv, previous_resp, *args, **kwargs):
    payload = iv + payload
    try:
        subprocess.check_output(['./padding_oracle.py', 'decrypt', payload.encode('hex')], stderr=None)
    except subprocess.CalledProcessError as e:
        return False, None
    return True, None


def test_decrypt(from_test=1):
    original_plaintext = "testItLongText siaxlla bam!"
    original_ciphertext = subprocess.check_output(
        ['./padding_oracle.py', 'encrypt', original_plaintext.encode('hex')]).strip().decode('hex')
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=True)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=True)
        assert decrypted == original_plaintext

    if from_test <= 2:
        data = original_ciphertext[:-block_size - 1] + 'A' + original_ciphertext[-block_size:]
        print "Test: cbc.decrypt(oracle, data, is_correct=False)"
        decrypted = cbc.decrypt(oracle, data, is_correct=False)
        assert decrypted[-block_size:-1] == original_plaintext[-block_size:-1]

    if from_test <= 3:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=False)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=False)
        assert decrypted[:-1] == original_plaintext[:-1]

    if from_test <= 4:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print "Test: cbc.decrypt(oracle, data, iv=iv)"
        decrypted = cbc.decrypt(oracle, data, iv=iv)
        assert decrypted == original_plaintext

    if from_test <= 5:
        print "Test: cbc.decrypt(oracle, original_ciphertext, amount=2)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, amount=2)
        assert decrypted == original_plaintext[-block_size * 2:]

    if from_test <= 6:
        print "Test: cbc.decrypt(oracle, original_ciphertext, amount=1, is_correct=True)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, amount=1, is_correct=True)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 7:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext)
        assert decrypted == original_plaintext

    if from_test <= 8:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-4:])"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-4:])
        assert decrypted == original_plaintext

    if from_test <= 9:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-7:], amount=1)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-7:], amount=1)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 10:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=False, known_plaintext=original_plaintext[-7:], amount=1)"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=False, known_plaintext=original_plaintext[-7:],
                                amount=1)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 11:
        print "Test: cbc.decrypt(oracle, original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-block_size-3:])"
        decrypted = cbc.decrypt(oracle, original_ciphertext, is_correct=True,
                                known_plaintext=original_plaintext[-block_size - 3:])
        assert decrypted == original_plaintext


def test_fake_ciphertext(from_test=1):
    new_plaintext = "Some other text we want to fake due to padding oracle."
    new_plaintext_padded = add_padding(new_plaintext, block_size)
    original_plaintext = "Whatever but length must be similar to new plaintext modulo16"
    original_ciphertext = subprocess.check_output(
        ['./padding_oracle.py', 'encrypt', original_plaintext.encode('hex')]).strip().decode('hex')
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print "Test: cbc.fake_ciphertext(oracle, new_plaintext_padded)"
        new_ciphertext = cbc.fake_ciphertext(oracle, new_plaintext_padded)
        decrypted = subprocess.check_output(
            ['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 2:
        print "Test: cbc.fake_ciphertext(oracle, new_plaintext, original_ciphertext=new_ciphertext)"
        new_ciphertext = cbc.fake_ciphertext(oracle, new_plaintext_padded, original_ciphertext=original_ciphertext)
        decrypted = subprocess.check_output(
            ['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 3:
        print "Test: cbc.fake_ciphertext(oracle, new_plaintext, original_ciphertext=original_ciphertext, original_plaintext=original_plaintext)"
        new_ciphertext = cbc.fake_ciphertext(oracle, new_plaintext_padded, original_ciphertext=original_ciphertext,
                                             original_plaintext=original_plaintext)
        decrypted = subprocess.check_output(
            ['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 4:
        print "Test: cbc.fake_ciphertext(oracle, new_plaintext, original_plaintext=original_plaintext)"
        new_ciphertext = cbc.fake_ciphertext(oracle, new_plaintext_padded, original_ciphertext=original_ciphertext,
                                             original_plaintext=original_plaintext[-3:])
        decrypted = subprocess.check_output(
            ['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 5:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print "Test: cbc.fake_ciphertext(oracle, new_plaintext, original_ciphertext=data, iv=iv)"
        new_ciphertext = cbc.fake_ciphertext(oracle, new_plaintext_padded, original_ciphertext=data, iv=iv)
        decrypted = subprocess.check_output(
            ['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext


test_decrypt(1)
test_fake_ciphertext(1)
