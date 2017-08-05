#!/use/bin/env sage


def pohlig_hellman(A, B, M, Pt, Qt, P_order_factors=None, n_max=None):
    '''Compute dicrete logarithm on Elliptic Curve using Pohlig-Hellman (order of P should be smooth)
    https://koclab.cs.ucsb.edu/teaching/ecc/project/2015Projects/Sommerseth+Hoeiland.pdf

    Elliptic Curve: y^2 = x^3 + A*x + B mod M
    Args:
        A,B,M(ints)
        Pt,Qt(tuples): Q = n*P
        n_max(int/None)

    Returns:
        n(int)

    Example:
        M = 93556643250795678718734474880013829509320385402690660619699653921022012489089

        A = 66001598144012865876674115570268990806314506711104521036747533612798434904785

        B = 25255205054024371783896605039267101837972419055969636393425590261926131199030

        Pt = (56027910981442853390816693056740903416379421186644480759538594137486160388926, 65533262933617146434438829354623658858649726233622196512439589744498050226926)

        Qt = (34492003315901643516027214681643546054021626043941009296234139428306204273023, 28634523416511300194166707350048820787265085824285526555863582510484829614250)

        n_max = 400000000000000000000000000000
    '''
    E = EllipticCurve(GF(M), [A,B])
    P = E(Pt)
    Q = E(Qt)

    P_order = P.order()
    if P_order_factors is None:
        P_order_factors = dict(P_order.factor())
        print P_order_factors
    modules = sorted([x for x in P_order_factors])

    modules_done = []
    residues = []
    n_recovered = 1
    for fac_one in modules:
        factor = fac_one^P_order_factors[fac_one]
        Px = P*long(P_order/fac_one)
        Qx = Q*long(P_order/fac_one)
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