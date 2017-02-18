import gmpy2
from CryptoAttacks.Utils import log
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


def product(numbers):
    if len(numbers) == 0:
        return 0
    if type(numbers) == list:
        return reduce(lambda x, y: x * y, numbers)
    elif type(numbers) == dict:
        return reduce(lambda x, y: x * (y**numbers[y]), numbers, 1)
    return False


def crt(a, n):
    """Solve chinese remainder theorem
    from: http://rosettacode.org/wiki/Chinese_remainder_theorem#Python

    Args:
        a(list): remainders
        n(list): modules

    Returns:
        long: solution to crt
    """
    if len(a) != len(n):
        log.critical_error("Different number of remainders({}) and modules({})".format(len(a), len(n)))

    prod = product(n)
    sum_crt = 0

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum_crt += a_i * invmod(p, n_i) * p
    return long(sum_crt % prod)


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
        while b:
            a, b = b, a % b
        return a
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
        return (a*b) / gcd(a, b)
    else:
        l = 1
        for number in args:
            l = lcm(l, number)
        return l


def factors(n):
    """Find factors of n
    from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    return set(reduce(list.__add__, ([i, n//i] for i in xrange(2, int(n**0.5) + 1) if n % i == 0)))


def egcd(*args):
    """Extended Euclidean algorithm"""
    if len(args) < 2:
        log.critical_error("Give at least two values")

    if len(args) == 2:
        a, b = args
        s0, t0, s1, t1 = 1, 0, 0, 1
        while b:
            q, a, b = a//b, b, a%b
            s0, s1 = s1, s0 - q*s1
            t0, t1 = t1, t0 - q*t1
        return a, s0, t0
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
    d, s, t = egcd(a, n)
    if d != 1:
        raise ValueError("Modular inverse doesn't exists ({}**(-1) % {})".format(a, n))
    return s % n

