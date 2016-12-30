import gmpy2
from GrosCrypto.Utils import log
import operator


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


def crt(a, n):
    """Chinese remainder theorem
    from: http://rosettacode.org/wiki/Chinese_remainder_theorem#Python

    Args:
        a(list): remainders
        n(list): modules

    Returns:
        long: solution to crt
    """
    if len(a) != len(n):
        log.critical_error("Different number of remainders({}) and modules({})".format(len(a), len(n)))

    sum = 0
    prod = reduce(lambda x, y: x * y, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * gmpy2.invert(p, n_i) * p
    return long(sum % prod)


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


def gcd(a, b):
    """Greatest common divisor"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Lowest common multiple"""
    return (a*b) / gcd(a, b)


def factors(n):
    """Find factors of n
    from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    return set(reduce(list.__add__, ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0)))
