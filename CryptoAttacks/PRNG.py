from CryptoAttacks.Utils import log
from CryptoAttacks.Math import gcd, invmod


class LCG(object):
    def __init__(self, seed, a, b, m):
        """Linear Congruence Generator

        Args:
            seed(int)
            a,b,m(ints): next_state = a*seed + b mod m
        """
        self.seed = seed
        self.a = a
        self.b = b
        self.m = m
        self.state = seed

    def next(self):
        """Returns next state"""
        new_state = (self.state*self.a + self.b) % self.m
        self.state = new_state
        return new_state

    def prev(self):
        """Returns previous state"""
        new_state = ((self.state - self.b) * invmod(self.a, self.m)) % self.m
        self.state = new_state
        return new_state

    @staticmethod
    def compute_params(s, m=None, a=None, b=None):
        """Compute parameters and initial seed for LCG prng
        next_state = a*state + b mod m

        Args:
            s(list): subsequent outputs from LCG oracle starting with seed
            m(int/None)
            a(int/None)
            b(int/None)

        Returns:
            a, b, m(int)
        """
        if m is None:
            t = [s[n + 1] - s[n] for n in range(len(s) - 1)]
            u = [abs(t[n + 2] * t[n] - t[n + 1] ** 2) for n in range(len(t) - 2)]
            m = gcd(*u)
            log.success("m = {}".format(m))

        if a is None:
            if gcd(s[1] - s[0], m) == 1:
                a = (s[2] - s[1]) * invmod(s[1] - s[0], m)
            elif gcd(s[2] - s[0], m) == 1:
                a = (s[3] - s[1]) * invmod(s[2] - s[0], m)
            else:
                log.critical_error("a not found")
            a = a % m
            log.success("a = {}".format(a))
            
        if b is None:
            b = (s[1] - s[0] * a) % m
            log.success("b = {}".format(b))
                
        return a, b, m
