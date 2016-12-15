import gmpy2
from Utils import log

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

