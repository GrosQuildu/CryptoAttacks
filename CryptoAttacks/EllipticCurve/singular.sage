def log_singular(f, p, P, Q):
    """Discrete logarithm on singular curve
    Q = d*P
    From: "Elliptic Curves: Number Theory and Cryptography, 2nd edition" by Washington (sec 2.10)

    Args:
        f(polynomial): curve equation (only x variable, may be over Rational Field)
            it is assumed that on left side of curve equation is y^2
        p(int): curve over finite field of size p
        P(tuple(int)): (x, y)
        Q(tuple(int)): (x, y)

    Returns:
        finite_rings.integer_mod: d
        tuple(finite_rings.integer_mod): (dx, dy)
    """
    # prepare stuff
    x,y = GF(p)['x,y'].gens()
    f = f.change_ring(GF(p))
    C = Curve(-y^2 + f)

    # find singular point
    singular_points = C.singular_points()
    if len(singular_points) != 1:
        if len(singular_points) == 0:
            print('No singular points')
        else:
            print('More than one singular point?')
        return

    # transform curve so that sp == (0,0)
    sp = singular_points[0]
    f_t = f.subs(x=x+sp[0], y=y+sp[1])
    print('Factorization of translated (singular point at (0,0)) f: {}'.format(f_t.factor()))

    # determine curve type
    curve_type = None
    factors = f_t.factor()
    if len(factors) == 2:
        if factors[0][1] == 2 and factors[0][0] == x:
            print('Curve is node')
            curve_type = 'node'
            a = factors[1][0].coefficients()[1]
        elif factors[1][1] == 2 and factors[1][0] == x:
            print('Curve is node')
            curve_type = 'node'
            a = factors[0][0].coefficients()[1]
        else:
            print('Something went wrong, singular point not at (0,0)')
    elif len(factors) == 1:
        if factors[0][1] == 3 and factors[0][0] == x:
            print('Curve is cusp')
            curve_type = 'cusp'
        else:
            print('Something went wrong, singular point not at (0,0)')
    else:
        print('Unknown curve type, not cusp nor node')

    # translate points to curve with sp == (0,0)
    P_t = map(GF(p), ((P[0]-sp[0]), (P[1]-sp[1])))
    Q_t = map(GF(p), ((Q[0]-sp[0]), (Q[1]-sp[1])))

    # compute discrete log
    if curve_type == 'node':
        d, D = log_node(p, P_t, Q_t, a)
    elif curve_type == 'cusp':
        d, D = log_cusp(P_t, Q_t)
    else:
        return

    # translate to original curve
    D = (D[0]+sp[0], D[1]+sp[1])

    return d, D


def log_cusp(P, Q):
    """Discrete logarithm on singular curve - cusp
    Assumption:
        Q = d*P
        y^2 = x^3
        singular point is (0,0)

    Args:
        P(tuple(finite_rings.integer_mod)): (x, y)
        Q(tuple(finite_rings.integer_mod)): (x, y)

    Returns:
        finite_rings.integer_mod: d
        tuple(finite_rings.integer_mod): (dx, dy)
    """
    # map points to additive group
    P_m = P[0] / P[1]
    Q_m = Q[0] / Q[1]

    # compute discrete log
    d = Q_m * (P_m^(-1))

    # map back to EC
    dx = d^(-2)
    dy = d^(-3)
    return d, (dx, dy)


def log_node(p, P, Q, a):
    """Discrete logarithm on singular curve - node
    Assumptions:
        Q = d*P
        y^2 = x^2 * (x+a)
        singular point is (0,0)

    Args:
        p(int): curve over finite field of size p
        P(tuple(finite_rings.integer_mod)): (x, y)
        Q(tuple(finite_rings.integer_mod)): (x, y)
        a(int): root of curve equation

    Returns:
        finite_rings.integer_mod: d
        tuple(finite_rings.integer_mod): (dx, dy)
    """
    # map points to multiplicative group
    a = GF(p)(a)
    if not a.is_square():
        print('a is not square')
        print('Not implemented yet, sorry')
        return None, None

    t = a.square_root()
    u = (P[1] + t*P[0]) / (P[1] - t*P[0])
    v = (Q[1] + t*Q[0]) / (Q[1] - t*Q[0])

    # compute discrete log
    d = v.log(u)

    # map back to EC
    dx = (4 * t^2 * d) / (d-1)^2
    dy = (4 * t^3 * d * (d+1)) / (d - 1)^3
    return d, (dx, dy)
