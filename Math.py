import gmpy2


def continued_fractions(n ,d):
    fractions = []
    r = 1
    while r:
        q = n // d
        r = n % d
        fractions.append(q)
        n, d = d, r
    return fractions

