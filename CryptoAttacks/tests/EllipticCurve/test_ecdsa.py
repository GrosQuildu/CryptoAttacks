
import sys
from hashlib import sha1

from CryptoAttacks.EllipticCurve.ecdsa import *
from CryptoAttacks.Utils import b2i, i2b
from sage.all_cmdline import *  # import sage library

_sage_const_3 = Integer(3); _sage_const_11279326 = Integer(11279326); _sage_const_182 = Integer(182); _sage_const_0 = Integer(0); _sage_const_12 = Integer(12); _sage_const_2 = Integer(2); _sage_const_85518893674295321206118380980485522083 = Integer(85518893674295321206118380980485522083); _sage_const_8 = Integer(8); _sage_const_1 = Integer(1); _sage_const_95051 = Integer(95051); _sage_const_40 = Integer(40); _sage_const_10 = Integer(10); _sage_const_16 = Integer(16); _sage_const_233970423115425145524320034830162017933 = Integer(233970423115425145524320034830162017933); _sage_const_20 = Integer(20); _sage_const_50 = Integer(50)



def hash_function_sha1(message):
    return b2i(sha1(message).digest())


def test_sign_verify():
    p = _sage_const_233970423115425145524320034830162017933 
    a = -_sage_const_95051 
    b = _sage_const_11279326 
    curve = EllipticCurve(Zmod(p), [a, b])
    G = curve(_sage_const_182 , _sage_const_85518893674295321206118380980485522083 )
    q = G.order()

    print "Test sign verify ECDSA"
    for _ in xrange(_sage_const_10 ):
        Q, d = generate_keys(G)
        message = randint(_sage_const_1 , long(q-_sage_const_1 ))
        r, s = sign(message, d, G)
        assert verify(message, (r, s), G, Q)

    print "Test sign verify ECDSA with hash function sha1"
    for _ in xrange(_sage_const_10 ):
        Q, d = generate_keys(G)
        message = i2b(randint(_sage_const_1 , long(q - _sage_const_1 )))
        r, s = sign(message, d, G, hash_function=hash_function_sha1)
        assert verify(message, (r, s), G, Q, hash_function=hash_function_sha1)


def sign_with_bias(message, d, G, l, hash_function=None):
    q = G.order()
    Zq = Zmod(q)

    r, s = _sage_const_0 , _sage_const_0 
    while s == _sage_const_0 :
        while r == _sage_const_0 :
            k = randint(_sage_const_1 , long(q - _sage_const_1 ))
            k = long(k & ~int((_sage_const_2 **l)-_sage_const_1 ))  # <- bias
            Q = (k * G)
            r = Q.xy()[_sage_const_0 ]

        if hash_function is None:
            s = (message + d * Zq(r)) * Zq(k) ** -_sage_const_1 
        else:
            s = (hash_function(message) + d * Zq(r)) * Zq(k) ** -_sage_const_1 
    return r, s


def test_recover_d_biased_k():
    p = _sage_const_233970423115425145524320034830162017933 
    a = -_sage_const_95051 
    b = _sage_const_11279326 
    curve = EllipticCurve(Zmod(p), [a, b])
    G = curve(_sage_const_182 , _sage_const_85518893674295321206118380980485522083 )
    q = G.order()

    print "Test recover private key from biased signatures"
    for _ in xrange(_sage_const_3 ):
        l = randint(_sage_const_16 , _sage_const_40 )
        messages, signatures = [], []
        Q, d = generate_keys(G)
        for _ in xrange(_sage_const_20 ):
            message = i2b(randint(_sage_const_1 , long(q - _sage_const_1 )))
            r, s = sign_with_bias(message, d, G, l, hash_function=hash_function_sha1)
            messages.append(message)
            signatures.append((long(r), long(s)))

        print 'with l = {}'.format(l)
        d_recovered = recover_d_biased_k(q, messages, signatures, l, hash_function=hash_function_sha1)
        assert d_recovered == d

    print "Test recover private key from biased signatures, smaller bias"
    success_count = _sage_const_0 
    trials = _sage_const_10 
    for _ in xrange(trials):
        l = randint(_sage_const_8 , _sage_const_12 )
        messages, signatures = [], []
        Q, d = generate_keys(G)
        for _ in xrange(_sage_const_50 ):
            message = randint(_sage_const_1 , long(q - _sage_const_1 ))
            r, s = sign_with_bias(message, d, G, l)
            messages.append(message)
            signatures.append((long(r), long(s)))

        print 'with l = {}'.format(l)
        d_recovered = recover_d_biased_k(q, messages, signatures, l)
        if d_recovered == d:
            success_count += _sage_const_1 
        print "Recovered {} / {}".format(success_count, trials)

if __name__ == "__main__":
    test_sign_verify()
    test_recover_d_biased_k()
