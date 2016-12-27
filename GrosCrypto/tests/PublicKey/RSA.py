#!/usr/bin/env python

import os
import subprocess

from GrosCrypto.PublicKey.RSA import *
from GrosCrypto.Utils import *

key_static_2048 = RSAKey.import_key("private_key_2048.pem")
key_static_1024 = RSAKey.import_key("private_key_1024.pem")
log.level = 'debug'


def test_wiener(tries=10):
    print "Test: wiener"
    for x in xrange(tries):
        n_size = 1024
        p = random_prime(n_size / 2)
        q = random_prime(n_size / 2)
        n = p*q
        phi = (p-1)*(q-1)
        while True:
            d = random.getrandbits(n_size / 4)
            if gmpy2.gcd(phi, d) == 1 and 81 * pow(d, 4) < n:
                break
        e = gmpy2.invert(d, phi)
        # print "e={}".format(e)
        # print "d={}".format(d)
        # print "n={}".format(n)
        key = RSAKey.construct(long(n), long(e))
        key_recovered = wiener(key.publickey())
        if key_recovered:
            assert key_recovered.d == d
        else:
            print "Not recovered"


def test_common_primes():
    print "Test: common primes"
    keys_path = "./common_prime/"
    keys = []
    for f in os.listdir(keys_path):
        if f.endswith('.pem'):
            tmp = RSAKey.import_key(keys_path+f)
            keys.append(tmp)
    priv_keys = common_primes(keys)
    assert len(priv_keys) != 0


def test_hastad():
    print "Test: hastad"
    n_size = 1024
    for e in [3, 17, 49]:
        print "Test: e={}".format(e)
        msg = random.randint(1000, 1 << (n_size-25))
        keys = []
        for count in xrange(e):
            tmp = RSAKey.generate(n_size, e=e).publickey()
            ciphertext = tmp.encrypt(msg, 0)[0]
            tmp.texts.append({'cipher': ciphertext})
            keys.append(tmp)
        msg_recovered = hastad(keys)
        assert msg_recovered == msg


def test_faulty():
    print "Test: faulty"
    for x in xrange(5):
        key = RSAKey.generate(1024)
        m = random.randint(0x13373371, key.n)
        sp = pow(m, key.d % (key.p - 1), key.p)
        sq = pow(m, key.d % (key.q - 1), key.q)
        sq_f = sq ^ random.randint(1, sq)  # random error

        s_f = crt([sp, sq_f], [key.p, key.q]) % key.n
        s = crt([sp, sq], [key.p, key.q]) % key.n

        key.texts.append({'cipher': s_f, 'plain': m})
        key_recovered = faulty(key.publickey())
        assert key_recovered and key_recovered.d == key.d

        key.texts = [{'cipher': s}, {'cipher': s_f}]
        key_recovered = faulty(key.publickey())
        assert key_recovered and key_recovered.d == key.d

        key.texts = [{'cipher': s}, {'cipher': s_f}, {'cipher': random.randint(1, key.n)},
                     {'cipher': random.randint(1, key.n), 'plain': random.randint(1, key.n)}]
        key_recovered = faulty(key.publickey())
        assert key_recovered and key_recovered.d == key.d

        key.texts = [{'cipher': s, 'plain': m}]
        key_recovered = faulty(key.publickey())
        assert key_recovered is False


def parity_oracle(ciphertext):
    ciphertext = i2b(ciphertext)
    message = subprocess.check_output(["./parity_oracle.py", "decrypt", ciphertext.encode('hex')]).strip().decode('hex')
    if message == '1':
        return 1
    return 0


def test_parity():
    print "Test: parity"
    plaintext = "Some plaintext " + random_str(10) + " anything can it be"
    ciphertext = subprocess.check_output(["./parity_oracle.py", "encrypt", plaintext.encode('hex')]).strip().decode('hex')

    key_static_1024.texts.append({'cipher': b2i(ciphertext)})
    msg_recovered = parity(parity_oracle, key_static_1024)
    assert msg_recovered == b2i(plaintext)
    key_static_1024.texts = []

test_parity()
test_faulty()
test_hastad()
test_common_primes()
test_wiener()
