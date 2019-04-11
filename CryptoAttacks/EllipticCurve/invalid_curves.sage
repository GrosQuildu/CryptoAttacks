#!/usr/bin/env sage


from sage.rings.finite_rings.integer_mod import square_root_mod_prime


def invalid_curves_oracle(point):
    """Oracle for invalid curves attack
        Should return point * secret_key in some form,
        so the output can be verified.
        In simplest form it should return {'x':x, 'y':y) dict (== point * secret_key)
    
    Args:
        point(EC point)

    Returns:
        Whatever, it will be passed to invalid_curves_verify
    """


def invalid_curves_verify(K, *args):
    """Verifier for invalid curves attack
        It should check if K == some_func(*args)
        In simplest form it should check if K.x == args[0].x and K.y == args[0].y
    
    Args:
        K(EC point)
        args(output from invalid_curves_oracle)

    Returns:
        Bool
    """


def generate_invalid_curves(P, A, B, max_factor, min_factor=16):
    """For curve EC == y^2 = x^3 + A*x + B find curves y^2 = x^3 + A*x + B2
        (differs only in B parameter), such that their orders have some small factors

    Args:
        P(int): EC filed
        A(int): EC param A
        B(int): EC param B
        max_factor(int): found curves must have order with
                            at least one factor such that: min_factor <= factor <= max_factor and factor power == 1
        min_factor(int):
    
    Returns:
        yields tuples: (EllipticCurve, EC order, small_factors)
    """
    B2 = 1
    while True:
        B2 += 1
        if B2 == B:
            continue

        try:
            EC2 = EllipticCurve(GF(P), [A, B2])
        except ArithmeticError as e:
            # probably singular curve
            print('Error {}'.format(e))
            continue

        order = EC2.order()
        small_factors = {}
        for one_factor in prime_range(min_factor, max_factor+1):
            if order % one_factor == 0 and order % (one_factor*one_factor) != 0:
                if min_factor <= one_factor <= max_factor:
                    small_factors[one_factor] = 1
        print('Have curve with B2={}'.format(B2))

        if len(small_factors) > 0:
            print('Yielding with {} small factors'.format(len(small_factors)))
            yield (EC2, order, small_factors)
        else:
            print('No small factors found')


def invalid_curves(EC, oracle, verify, curves=generate_invalid_curves, bound=None, max_factor=65536, min_factor=16, max_attempts=5000):
    """Invalid curves attack
        When somebody computes your_point * secret_key without checking if your_point lies on the curve

        If you use generate_invalid_curves (default function) and the secret key is not found:
        save generated primes as list (they are printed), generate more curves,
         add them to the list and run this function with curves == the list

    Args:
        EC(EllipticCurve)
        oracle(function): like invalid_curves_oracle
        verify(function): like invalid_curves_verify
        curves(list/generator): list of tuples (Elliptic Curve, order, small_factors) (EC, int, dict)
                                or generator returning such tuples
                                Curves must differ only in b component
        bound(int/None): compute secret modulo bound, default bound == P
                            if there are not enough small factors on the curves,
                            secret will be computed modulo something smaller
        max_factor(int/None): all factors in small_factors will be <= max_factor
        min_factor(int/None): all factors in small_factors will be >= min_factor
        max_attempts(int): limit random point generation

    Returns
        tuple(int,int): secret key % bound_reached, bound_reached
    """
    print("Invalid curves attack")
    P = EC.base_field().order()

    if not bound:
        bound = P

    used_already = []
    remainders = []
    modules = []
    curve_counter = 0

    # generate invalid curves
    if type(curves) != list:
        print('Generating invalid curves')
        curves_generator = curves
        curves = []
        curves_factors_product = 1
        for EC2, order, factors in curves_generator(P, EC.a4(), EC.a6(), max_factor):
            curves.append((EC2, order, factors))
            curves_factors_product *= product(list(factors))
            print('Invalid curves factors product: {} / {}'.format(curves_factors_product, bound))
            if curves_factors_product >= bound:
                break

    print('Invalid to use curves:')
    print('[')
    for EC2, order, factors in curves:
        print('(EllipticCurve(GF({}), [{},{}]), {}, {}),'.format(P, EC2.a4(), EC2.a6(), order, factors))
    print(']')

    # iterate over curves until we are done
    while product(modules) < bound:

        # small factors are not enough, use big factors
        if curve_counter >= len(curves):
            # whopse, big factors are also not enough
            if max_factor == infinity:
                print('Not enough factors')
                break
            curve_counter = 0
            max_factor = infinity

        # get the curve from the list
        print("Use curve no {}".format(curve_counter))
        current_curve = curves[curve_counter][0]
        curve_order = curves[curve_counter][1]
        curve_order_factors = curves[curve_counter][2]

        # iterate over curve's factors
        for curve_order_factor in sorted(curve_order_factors):
            if curve_order_factor > max_factor:
                curve_counter += 1
                break

            # skip factors with power > 1 and repeated factors
            print("r{} == {}".format(len(remainders), curve_order_factor))
            if curve_order_factor < min_factor or curve_order_factors[curve_order_factor] != 1 or curve_order_factor in used_already:
                print("Skip above")
                continue
            used_already.append(curve_order_factor)

            # find point h on insecure curve with order == small factor
            found_x_y_pair = False
            found_point = False

            attempts = 0
            while not found_point and attempts <= max_attempts:
                while not found_x_y_pair:
                    x = Zmod(P)(randint(1, P-1))
                    y2 = x^3 + current_curve.a4()*x + current_curve.a6()
                    y = square_root_mod_prime(y2, P)
                    if y^2 == y2:
                        found_x_y_pair = True

                attempts += 1
                rand_point = current_curve(x, y)
                h = rand_point * (curve_order//curve_order_factor)
                if not h.is_zero():
                    assert (h*curve_order_factor).is_zero()  # h has order curve_order_factor 
                    assert h.order() == curve_order_factor
                    found_point = True

            # get oracle_output == some_func(h*secret)
            oracle_output = oracle(h)

            K = h
            for maybe_secret in range(1, curve_order_factor):
                # K == h * maybe_secret
                # check if some_func(K) == some_func(h*secret)
                if verify(K, current_curve, *oracle_output):
                    print("Got secret%{} == {}".format(curve_order_factor, maybe_secret))
                    remainders.append(maybe_secret)
                    modules.append(curve_order_factor)
                    break
                K += h
            else:
                print("Strange: K not found for r == {}".format(curve_order_factor))

            # curve_counter += 1
            if product(modules) >= bound:
                break

        curve_counter += 1

    secret_key = crt(remainders, modules)
    bound_reached = product(modules)
    print("Secret key found: secret_key%{} == {}".format(bound_reached, secret_key))
    return int(secret_key), int(bound_reached)
