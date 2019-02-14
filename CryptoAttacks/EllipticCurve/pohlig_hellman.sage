#!/use/bin/env sage


def pohlig_hellman(A, B, M, Pt, Qt, P_order_factors=None, n_max=None):
    '''Compute dicrete logarithm on Elliptic Curve using Pohlig-Hellman (order of P should be smooth)
    https://koclab.cs.ucsb.edu/teaching/ecc/project/2015Projects/Sommerseth+Hoeiland.pdf

    y^2 = x^3 + A*x + B mod M
    Q = n*P

    Args:
        A, B, M(int)
        Pt, Qt(tuple) 
        P_order_factors(dict/None)
        n_max(int/None)

    Returns:
        n(int)
    '''
    # prepare stuff
    E = EllipticCurve(GF(M), [A,B])
    P = E(Pt)
    Q = E(Qt)

    # factor P order
    P_order = P.order()
    if P_order_factors is None:
        P_order_factors = dict(P_order.factor())
        print('P order factors: {}'.format(P_order_factors))
    modules = sorted([x for x in P_order_factors])

    modules_done = []
    residues = []
    n_recovered = 1
    for fac_one in modules:
        factor = fac_one^P_order_factors[fac_one]
        Px = P*int(P_order/fac_one)
        Qx = Q*int(P_order/fac_one)
        l = Px.discrete_log(Qx)
        residues.append(l)
        modules_done.append(factor)
        n_recovered *= factor
        print 'n%{} == {}'.format(factor, l)
        if n_max is not None and n_recovered >= n_max:
            break

    # print residues
    # print modules_done
    n = crt(residues, modules_done)
    return n
