# Math

```python
def crt(a, n):
    """Solve chinese remainder theorem
    from: http://rosettacode.org/wiki/Chinese_remainder_theorem#Python

    Args:
        a(list): remainders
        n(list): modules

    Returns:
        long: solution to crt
    """


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


def euler_phi(factors):
    """Compute euler's phi (totient) function

    Args:
        factors(dict/list): if dict: factorization of n, {p1: k1, p2: k2} <- n == p1**k1 * p2**k2
                            if list: [p1, p2] <- n == p1*p2

    Returns:
        int
    """


def gcd(*args):
    """Greatest common divisor"""


def lcm(*args):
    """Lowest common multiple"""


def egcd(*args):
    """Extended Euclidean algorithm"""


def invmod(a, n):
    """Modular inverse. a*invmod(a) == 1 (mod n)"""


def factors(n):
    """Find factors of n
    from http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """

def legendre(a, p):
    """Legendre symbol"""

def tonelli_shanks(n, p):
    """Find r such that r^2 = n % p, r2 == p-r"""
```
