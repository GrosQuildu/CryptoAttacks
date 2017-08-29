import sys
sys.path.append('../../EllipticCurve')
from ecdsa_sage import *

from hashlib import sha1
from CryptoAttacks.Utils import i2b, b2i


def hash_function_sha1(message):
    return b2i(sha1(message).digest())


def test_sign_verify():
    p = 233970423115425145524320034830162017933
    a = -95051
    b = 11279326
    curve = EllipticCurve(Zmod(p), [a, b])
    G = curve(182, 85518893674295321206118380980485522083)
    q = G.order()

    print "Test sign verify ECDSA"
    for _ in xrange(10):
        Q, d = generate_keys(G)
        message = randint(1, long(q-1))
        r, s = sign(message, d, G)
        assert verify(message, (r, s), G, Q)

    print "Test sign verify ECDSA with hash function sha1"
    for _ in xrange(10):
        Q, d = generate_keys(G)
        message = i2b(randint(1, long(q - 1)))
        r, s = sign(message, d, G, hash_function=hash_function_sha1)
        assert verify(message, (r, s), G, Q, hash_function=hash_function_sha1)


def sign_with_bias(message, d, G, l, hash_function=None):
    q = G.order()
    Zq = Zmod(q)

    r, s = 0, 0
    while s == 0:
        while r == 0:
            k = randint(1, long(q - 1))
            k = long(k & ~int((2^l)-1))  # <- bias
            Q = (k * G)
            r = Q.xy()[0]

        if hash_function is None:
            s = (message + d * Zq(r)) * Zq(k) ^ -1
        else:
            s = (hash_function(message) + d * Zq(r)) * Zq(k) ^ -1
    return r, s


def test_recover_d_biased_k():
    p = 233970423115425145524320034830162017933
    a = -95051
    b = 11279326
    curve = EllipticCurve(Zmod(p), [a, b])
    G = curve(182, 85518893674295321206118380980485522083)
    q = G.order()

    print "Test recover private key from biased signatures"
    for _ in xrange(3):
        l = randint(16, 40)
        messages, signatures = [], []
        Q, d = generate_keys(G)
        for _ in xrange(20):
            message = i2b(randint(1, long(q - 1)))
            r, s = sign_with_bias(message, d, G, l, hash_function=hash_function_sha1)
            messages.append(message)
            signatures.append((long(r), long(s)))

        print 'with l = {}'.format(l)
        d_recovered = recover_d_biased_k(q, messages, signatures, l, hash_function=hash_function_sha1)
        assert d_recovered == d

    print "Test recover private key from biased signatures, smaller bias"
    success_count = 0
    trials = 10
    for _ in xrange(trials):
        l = randint(8, 12)
        messages, signatures = [], []
        Q, d = generate_keys(G)
        for _ in xrange(50):
            message = randint(1, long(q - 1))
            r, s = sign_with_bias(message, d, G, l)
            messages.append(message)
            signatures.append((long(r), long(s)))

        print 'with l = {}'.format(l)
        d_recovered = recover_d_biased_k(q, messages, signatures, l)
        if d_recovered == d:
            success_count += 1
        print "Recovered {} / {}".format(success_count, trials)

if __name__ == "__main__":
    test_sign_verify()
    test_recover_d_biased_k()