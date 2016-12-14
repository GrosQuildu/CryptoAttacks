#!/usr/bin/python

from Utils import *
from Block.cbc import PaddingOracle
from Crypto.Cipher import AES
import subprocess

log.level = 'info'
block_size = AES.block_size


class Padding(PaddingOracle):
    def oracle(self, payload, iv, previous_resp, *args, **kwargs):
        payload = iv + payload
        try:
            ret = subprocess.check_output(['./padding_oracle.py', 'decrypt', payload.encode('hex')], stderr=None)
        except subprocess.CalledProcessError as e:
            return False, None
        return True, None

po = Padding(block_size)


def test_decrypt(from_test=1):
    original_plaintext = "testItLongText siaxlla bam!"
    original_ciphertext = subprocess.check_output(
        ['./padding_oracle.py', 'encrypt', original_plaintext.encode('hex')]).strip().decode('hex')
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print "Test: po.decrypt(original_ciphertext, is_correct=True)"
        decrypted = po.decrypt(original_ciphertext, is_correct=True)
        assert decrypted == original_plaintext

    if from_test <= 2:
        data = original_ciphertext[:-block_size-1] + 'A' + original_ciphertext[-block_size:]
        print "Test: po.decrypt(data, is_correct=False)"
        decrypted = po.decrypt(data, is_correct=False)
        assert decrypted[-block_size:-1] == original_plaintext[-block_size:-1]

    if from_test <= 3:
        print "Test: po.decrypt(original_ciphertext, is_correct=False)"
        decrypted = po.decrypt(original_ciphertext, is_correct=False)
        assert decrypted[:-1] == original_plaintext[:-1]

    if from_test <= 4:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print "Test: po.decrypt(data, iv=iv)"
        decrypted = po.decrypt(data, iv=iv)
        assert decrypted == original_plaintext

    if from_test <= 5:
        print "Test: po.decrypt(original_ciphertext, amount=2)"
        decrypted = po.decrypt(original_ciphertext, amount=2)
        assert decrypted == original_plaintext[-block_size*2:]

    if from_test <= 6:
        print "Test: po.decrypt(original_ciphertext, amount=1, is_correct=True)"
        decrypted = po.decrypt(original_ciphertext, amount=1, is_correct=True)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 7:
        print "Test: po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext)"
        decrypted = po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext)
        assert decrypted == original_plaintext

    if from_test <= 8:
        print "Test: po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-4:])"
        decrypted = po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-4:])
        assert decrypted == original_plaintext

    if from_test <= 9:
        print "Test: po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-7:], amount=1)"
        decrypted = po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-7:], amount=1)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 10:
        print "Test: po.decrypt(original_ciphertext, is_correct=False, known_plaintext=original_plaintext[-7:], amount=1)"
        decrypted = po.decrypt(original_ciphertext, is_correct=False, known_plaintext=original_plaintext[-7:], amount=1)
        assert decrypted == original_plaintext[-block_size:]

    if from_test <= 11:
        print "Test: po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-block_size-3:])"
        decrypted = po.decrypt(original_ciphertext, is_correct=True, known_plaintext=original_plaintext[-block_size-3:])
        assert decrypted == original_plaintext


def test_fake_ciphertext(from_test=1):
    new_plaintext = "Some other text we want to fake due to padding oracle."
    new_plaintext_padded = add_padding(new_plaintext, block_size)
    original_plaintext = "Whatever but length must be similar to new plaintext modulo16"
    original_ciphertext = subprocess.check_output(
        ['./padding_oracle.py', 'encrypt', original_plaintext.encode('hex')]).strip().decode('hex')
    original_plaintext = add_padding(original_plaintext, block_size)

    if from_test <= 1:
        print "Test: po.fake_ciphertext(new_plaintext_padded)"
        new_ciphertext = po.fake_ciphertext(new_plaintext_padded)
        decrypted = subprocess.check_output(['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 2:
        print "Test: po.fake_ciphertext(new_plaintext, original_ciphertext=new_ciphertext)"
        new_ciphertext = po.fake_ciphertext(new_plaintext_padded, original_ciphertext=original_ciphertext)
        decrypted = subprocess.check_output(['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 3:
        print "Test: po.fake_ciphertext(new_plaintext, original_ciphertext=original_ciphertext, original_plaintext=original_plaintext)"
        new_ciphertext = po.fake_ciphertext(new_plaintext_padded, original_ciphertext=original_ciphertext, original_plaintext=original_plaintext)
        decrypted = subprocess.check_output(['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 4:
        print "Test: po.fake_ciphertext(new_plaintext, original_plaintext=original_plaintext)"
        new_ciphertext = po.fake_ciphertext(new_plaintext_padded, original_ciphertext=original_ciphertext, original_plaintext=original_plaintext[-3:])
        decrypted = subprocess.check_output(['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

    if from_test <= 5:
        iv = original_ciphertext[:block_size]
        data = original_ciphertext[block_size:]
        print "Test: po.fake_ciphertext(new_plaintext, original_ciphertext=data, iv=iv)"
        new_ciphertext = po.fake_ciphertext(new_plaintext_padded, original_ciphertext=data, iv=iv)
        decrypted = subprocess.check_output(['./padding_oracle.py', 'decrypt', new_ciphertext.encode('hex')]).strip().decode('hex')
        assert decrypted == new_plaintext

test_decrypt(1)
test_fake_ciphertext(1)
