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

    r, s = 0, 0
    while s == 0:
        while r == 0:
            k = randint(1, long(q - 1))
            Q = (k * G)
            r = Q.xy()[0]

        if hash_function is None:
            s = (message + d * Zq(r)) * Zq(k) ^ -1
        else:
            s = (hash_function(message) + d * Zq(r)) * Zq(k) ^ -1
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

    w = Zq(s) ^ -1
    if hash_function is None:
        u1 = Integer(message * w)
    else:
        u1 = Integer(hash_function(message) * w)
    u2 = Integer(Zq(r) * w)

    x1 = (u1*G + u2*Q).xy()[0]
    x2 = (u1*G - u2*Q).xy()[0]
    return r == x1 or r == x2


def generate_keys(G):
    """Generate ECDSA keys

    Args:
        G(EllipticCurvePoint_finite_field): base point

    Returns:
        public key, private key
    """
    secret = randint(2, G.order()-1)
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
        t = r / (s * 2 ^ l)
        if hash_function is None:
            u = message / (-s * 2 ^ l)
        else:
            u = hash_function(message) / (-s * 2 ^ l)
        bt.append(long(t))
        bu.append(long(u))
        mtr.append([0] * i + [q] + [0] * (len(signatures) - i - 1 + 2))

    ct = 1 / 2 ^ l
    cu = q / 2 ^ l
    bt.extend([ct, 0])
    bu.extend([0, cu])

    mtr.append(bt)
    mtr.append(bu)

    matrix_ecdsa = matrix(mtr)
    if len(signatures) <= 20:
        print '-----matrix------'
        for i in xrange(len(signatures) + 2):
            print matrix_ecdsa[i]

    print 'Will be looking for {}'.format(cu)

    lll = matrix_ecdsa.LLL()
    dct, d_recovered = None, None

    print '-----last entries LLL basis-------'
    for i in xrange(len(signatures) + 2):
        print '{} {}'.format(lll[i][-2], lll[i][-1])
        if lll[i][-1] == cu:
            dct = lll[i][-2]
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


def dsks(G, message, signature, Q, hash_function):
    """Duplicate-Signature Key Selection in ECDSA
    Create key pair and domain parameter G that verifies given signature

    So if we have someone public key Q and signature (r,s) of some message signed
    with corresponding private key we can create new key pair that will verify
    the signature IF we also change base point G 


    Args:
        G(EllipticCurvePoint_finite_field): base point
        message(int/arg for hash_function)
        signature(tuple(int)): (r,s), signature of m
        Q(int): public key
        hash_function(NoneType/callable)

    Returns:
        G'(EllipticCurvePoint_finite_field): new base point
        d'(int): new private key
        Q'(EllipticCurvePoint_finite_field): new public key, Q = d*G
    """
    m = message
    r, s = map(int, signature)

    if hash_function is None:
        u1 = (m * inverse_mod(s, G.order())) % G.order()
    else:
        u1 = (hash_function(m) * inverse_mod(s, G.order())) % G.order()
    u2 = (r * inverse_mod(s, G.order())) % G.order()
    R = u1*G + u2*Q

    d_p = randint(1, G.order()-1)
    t = u1 + u2*d_p
    G_p = R * inverse_mod(t, G.order())
    Q_p = d_p * G_p
    if verify(message, signature, G_p, Q_p, hash_function):
        return G_p, d_p, Q_p

    R = u1*G - u2*Q  # lose of y in ledder
    G_p = R * inverse_mod(t, G.order())
    Q_p = d_p * G_p
    G_p.order = G.order()
    return G_p, d_p, Q_p
