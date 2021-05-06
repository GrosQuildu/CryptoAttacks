from __future__ import absolute_import, division, print_function

import operator
from builtins import int, pow, range, zip
from functools import reduce
import math

from Crypto.Util.number import isPrime, getPrime

from CryptoAttacks.Utils import log


def continued_fractions(n, d):
    fractions = []
    r = 1
    while r:
        q = n // d
        r = n % d
        fractions.append(q)
        n, d = d, r
    return fractions


def convergents(e):
    """ from https://sagi.io/2016/04/crypto-classics-wieners-rsa-attack/#fn:6bca21c36a35b17c8f971fe0bb59ec27:2 """
    n = []  # Nominators
    d = []  # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else:  # i > 1
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)


def product(numbers):
    if len(numbers) == 0:
        return 0
    elif type(numbers) == dict:
        return reduce(lambda x, y: x * (y**numbers[y]), numbers, 1)
    else:
        try:
            return reduce(lambda x, y: x * y, numbers)
        except:
            pass
    return False


def crt(a, n):
    """Solve chinese remainder theorem
    from: http://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    The solution will be modulo product of modules

    Args:
        a(list): remainders
        n(list): modules

    Returns:
        int: solution to crt
    """
    if len(a) != len(n):
        log.critical_error("Different number of remainders({}) and modules({})".format(len(a), len(n)))

    prod = product(n)
    sum_crt = 0

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum_crt += a_i * invmod(p, n_i) * p
    return int(sum_crt % prod)


def crt_non_coprime(a, n):
    """Solve chinese remainder theorem with general modules
    Given:
    x = a % n
    x = b % m

    If modules n, m are not comprime, but a = b mod gcd(n, m) then solution can be found
    The solution will be modulo lcm of modules

    Args:
        a(list): remainders
        n(list): modules

    Returns:
        int: solution to crt
    """
    if len(a) != len(n):
        log.critical_error("Different number of remainders({}) and modules({})".format(len(a), len(n)))

    if len(n) < 2:
        log.critical_error("Give at least two remainders and modules (got {})".format(len(n)))

    while len(n) > 1:
        g, u, _ = egcd(n[0], n[1])

        if (a[0] - a[1]) % g != 0:
            print('Not satisfied: gcd(ni, nj) | ai - aj\ngcd({}, {}) | {} - {}'.format(n[0], n[1], a[0], a[1]))
            return None

        w = (a[0] - a[1]) // g
        l = lcm(n[0], n[1])
        x = (a[0] - n[0]*u*w) % l

        n = n[2:]
        n.insert(0, l)
        a = a[2:]
        a.insert(0, x)

    return int(a[0] % n[0])


def euler_phi(factors):
    """Compute euler's phi (totient) function
    
    Args:
        factors(dict/list): if dict: factorization of n, {p1: k1, p2: k2} <- n == p1**k1 * p2**k2
                            if list: [p1, p2] <- n == p1*p2

    Returns:
        int
    """
    if type(factors) == dict:
        return reduce(operator.mul, [(p**(factors[p]-1)) * (p - 1) for p in factors])
    else:
        return reduce(operator.mul, [p-1 for p in factors])


def gcd(*args):
    """Greatest common divisor"""
    if len(args) < 2:
        log.critical_error("Give at least two values")

    if len(args) == 2:
        a, b = args
        return gmpy2.gcd(a, b)
    else:
        d = 0
        for number in args:
            d = gcd(d, number)
            if d == 1:
                break
        return d


def lcm(*args):
    """Lowest common multiple"""
    if len(args) < 2:
        log.critical_error("Give at least two values")

    if len(args) == 2:
        a, b = args
        return gmpy2.lcm(a, b)
    else:
        l = 1
        for number in args:
            l = lcm(l, number)
        return l


def factors(n):
    """Find factors of n
    from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))


def egcd(*args):
    """Extended Euclidean algorithm"""
    if len(args) < 2:
        log.critical_error("Give at least two values")

    if len(args) == 2:
        a, b = args
        return gmpy2.gcdext(a, b)
    else:
        d, s, t = egcd(args[0], args[1])
        coefficients = [s, t]
        for i in range(2, len(args)):
            d, s, t = egcd(d, args[i])
            for j in range(len(coefficients)):
                coefficients[j] *= s
            coefficients.append(t)
        coefficients.insert(0, d)
        return coefficients


def invmod(a, n):
    """Modular inverse. a*invmod(a) == 1 (mod n)"""
    return gmpy2.invert(a, n)

def legendre(a, p):
    """Legendre symbol"""
    tmp = gmpy2.powmod(a, (p-1)//2, p)
    return -1 if tmp == p-1 else tmp


def tonelli_shanks(n, p):
    """Find r such that r^2 = n % p, r2 == p-r"""
    if legendre(n, p) != 1:
        log.critical_error("Not a square root")

    s = 0
    q = p-1
    while q & 1 == 0:
        s += 1
        q >>= 1

    if s == 1:
        return gmpy2.powmod(n, (p+1)//4, p)

    z = 1
    while legendre(z, p) != -1:
        z += 1
    c = gmpy2.powmod(z, q, p)

    r = gmpy2.powmod(n, (q+1)//2, p)
    t = gmpy2.powmod(n, q, p)
    m = s
    while t != 1:
        i = 1
        while i < m:
            if gmpy2.powmod(t, 2**i, p) == 1:
                break
            i += 1
        b = gmpy2.powmod(c, 2**(m-i-1), p)
        r = (r*b) % p
        t = (t * (b**2)) % p
        c = gmpy2.powmod(b, 2, p)
        m = i
    return r


def find_generator(p, factors):
    """Find generator of cyclic group of order p-1
    
    Args:
        p(int)
        factors(dict): factorization of p-1, {2:3, 17:1,}

    Returns:
        int: generator of Zp*
    """
    g = 1
    for one_factor in factors:
        b = 1
        while b != 1:
            a = randint(3, p-1)
            if gcd(a, p-1) != 1:
                continue
            b = gmpy2.powmod(a, (p-1)//one_factor, p)
        y = gmpy2.powmod(a, (p-1)//(one_factor**factors[one_factor]), p)
        g *= y
    return g


def generate_smooth_prime(bit_size, primitive_roots=[], smooth_bit_size=50, exclude=[]):
    """Generate smooth prime n

    Args:
        bit_size(int): size of generated prime in bits
        primitive_roots(list(int)): list of numbers that will be primitive roots modulo n
        smooth_bit_size(int): most factors of n-1 will be of this bit size   
        exclude(list(int)): n-1 won't have any factor from that list

    Returns:
        int: n
    """
    while True:
        n = 2
        factors = {2:1}

        # get random primes of correct size
        log.debug('smooth prime - loop of size about {}'.format((bit_size - 2*smooth_bit_size)//smooth_bit_size))
        while n.bit_length() < bit_size - 2*smooth_bit_size:
            q = getPrime(smooth_bit_size)
            if q in exclude:
                continue
            n *= q
            if q in factors:
                factors[q] += 1
            else:
                factors[q] = 1

        # find last prime so that n+1 is prime and the size is correct
        smooth_bit_size_padded = bit_size - n.bit_length()
        log.debug('smooth prime - smooth_bit_size_padded = {}'.format(smooth_bit_size_padded))
        while True:
            q = getPrime(smooth_bit_size_padded)
            if q in exclude:
                continue
            if isPrime((n*q)+1):
                n = (n*q)+1
                if q in factors:
                    factors[q] += 1
                else:
                    factors[q] = 1
                break
        
        # check if given numbers are primitive roots
        log.debug('smooth prime - checking primitive roots')
        are_primitive_roots = True
        if len(primitive_roots) > 0: 
            for factor, factor_power in factors.items():
                for primitive_root in primitive_roots:
                    if gmpy2.powmod(primitive_root, (n-1)//(factor**factor_power), n) == 1:
                        are_primitive_roots = False
                        break

        if are_primitive_roots:
            log.debug('smooth prime - done')
            return n, factors
        else:
            log.debug('primitive roots criterion not met')


def babystep_giantstep(g, h, p, upper_bound):
    m = int(math.ceil(math.sqrt(upper_bound)))
    log.debug('babystep-giantstep with loops of size {}'.format(m))
    g_j = {}
    g_j_tmp = 1
    for j in range(m):
        g_j[g_j_tmp] = j
        g_j_tmp = (g_j_tmp*g) % p

    g_m = invmod(gmpy2.powmod(g, m, p), p)
    y = h
    for i in range(m):
        if y in g_j:
            return (i*m + g_j[y]) % p
        y = (y*g_m) % p


def pohlig_hellman(g, h, n, n_order_factors):
    """Pohlig-Hellman discrete logarithm method (with babystep-giantstep)
    g^x == h % n

    Args:
        g, h, n(int)
        n_order_factors(dict): factors of n's order (euler_phi(n))

    Returns:
        int: x
    """
    no = product(n_order_factors)
    xi = []
    ci, loop_size = 1, len(n_order_factors.keys())
    for pi, ei in n_order_factors.items():
        log.debug('Pohlig-Hellman iteration {}/{}'.format(ci, loop_size))
        ci += 1

        gi = gmpy2.powmod(g, no//(pi**ei), n)  # gi have order pi**ei
        hi = gmpy2.powmod(h, no//(pi**ei), n)  # hi is in <gi>

        xk = 0
        gamma = gmpy2.powmod(gi, pi**(ei-1), n)  # gamma has order pi
        for k in range(ei):
            hk = invmod(gmpy2.powmod(gi, xk, n), n)
            hk = gmpy2.powmod(hk * hi, pi**(ei-1-k), n)  # hk is in <gamma>
            dk = babystep_giantstep(gamma, hk, n, pi)
            if dk is None:
                return None
            xk = (xk + gmpy2.powmod(pi, k, pi**ei)*dk) % (pi**ei)
        xi.append(xk)
        
    return crt(xi, [pi**ei for pi, ei in n_order_factors.items()])
