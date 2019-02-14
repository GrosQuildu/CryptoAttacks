
from sage.all_cmdline import *  # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_20 = Integer(20)
def sign(message, d, G, hash_function=None):
    """Sign ECDSA

    Args:
        message(int/arg for hash_function)
        d(int): private key
        G(EllipticCurvePoint_finite_field): base point
        hash_function(NoneType/callable)

    Returns:
        r,s
    """
    q = G.order()
    Zq = Zmod(q)

    r, s = _sage_const_0 , _sage_const_0 
    while s == _sage_const_0 :
        while r == _sage_const_0 :
            k = randint(_sage_const_1 , long(q - _sage_const_1 ))
            Q = (k * G)
            r = Q.xy()[_sage_const_0 ]

        if hash_function is None:
            s = (message + d * Zq(r)) * Zq(k) ** -_sage_const_1 
        else:
            s = (hash_function(message) + d * Zq(r)) * Zq(k) ** -_sage_const_1 
    return r, s


def verify(message, signature, G, Q, hash_function=None):
    """Verify ECDSA signature

    Args:
        message(int/arg for hash_function)
        signature(tuple of ints): r, s
        G(EllipticCurvePoint_finite_field): base point
        Q(EllipticCurvePoint_finite_field): public key
        hash_function(NoneType/callable)

    Returns:
        True/False
    """
    q = G.order()
    Zq = Zmod(q)
    r, s = signature

    w = Zq(s) ** -_sage_const_1 
    if hash_function is None:
        u1 = Integer(message * w)
    else:
        u1 = Integer(hash_function(message) * w)
    u2 = Integer(Zq(r) * w)

    x1 = (u1*G + u2*Q).xy()[_sage_const_0 ]
    x2 = (u1*G - u2*Q).xy()[_sage_const_0 ]
    return r == x1 or r == x2


def generate_keys(G):
    """Generate ECDSA keys

    Args:
        G(EllipticCurvePoint_finite_field): base point

    Returns:
        public key, private key
    """
    secret = randint(_sage_const_2 , G.order()-_sage_const_1 )
    return G*secret, Zmod(G.order())(secret)


def recover_d_biased_k(q, messages, signatures, l, hash_function=None):
    """Recover ECDSA private key from message/signature pairs, when k (emphemeral key) lsb are biased to 0

    Args:
        q(int): base point's order
        messages(list)
        signatures(list): [(r,s), (r,s)]
        l(int): amount of bits biased to 0 in k (lsb)
        hash_function(NoneType/callable)

    Returns:
        private key(int)
    """
    if len(messages) != len(signatures):
        print "Amount of signatures must equal amount of messages"
        return None

    print 'Preparing matrix'
    Zq = Zmod(q)
    bt, bu, mtr = [], [], []
    for i, (message, signature) in enumerate(zip(messages, signatures)):
        r, s = signature
        r, s = Zq(r), Zq(s)
        t = r / (s * _sage_const_2  ** l)
        if hash_function is None:
            u = message / (-s * _sage_const_2  ** l)
        else:
            u = hash_function(message) / (-s * _sage_const_2  ** l)
        bt.append(long(t))
        bu.append(long(u))
        mtr.append([_sage_const_0 ] * i + [q] + [_sage_const_0 ] * (len(signatures) - i - _sage_const_1  + _sage_const_2 ))

    ct = _sage_const_1  / _sage_const_2  ** l
    cu = q / _sage_const_2  ** l
    bt.extend([ct, _sage_const_0 ])
    bu.extend([_sage_const_0 , cu])

    mtr.append(bt)
    mtr.append(bu)

    matrix_ecdsa = matrix(mtr)
    if len(signatures) <= _sage_const_20 :
        print '-----matrix------'
        for i in xrange(len(signatures) + _sage_const_2 ):
            print matrix_ecdsa[i]

    print 'Will be looking for {}'.format(cu)

    lll = matrix_ecdsa.LLL()
    dct, d_recovered = None, None

    print '-----last entries LLL basis-------'
    for i in xrange(len(signatures) + _sage_const_2 ):
        print '{} {}'.format(lll[i][-_sage_const_2 ], lll[i][-_sage_const_1 ])
        if lll[i][-_sage_const_1 ] == cu:
            dct = lll[i][-_sage_const_2 ]
            # break

    if dct is not None:
        # dct == -d*ct == -d/2^l
        print '-d*ct = {} ({})'.format(dct, dct % q)
        d = (-dct / ct) % q
        print 'd = {}'.format(d)
        return d
    else:
        print 'Not found'
        return None
