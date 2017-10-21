# PRNG

```python
class LCG(object):
    def __init__(self, seed, a, b, m):
        """Linear Congruence Generator

        Args:
            seed(int)
            a,b,m(ints): next_state = a*state + b mod m
        """
    def next(self):
        """Returns next state"""

    def prev(self):
        """Returns previous state"""

    @staticmethod
    def compute_params(s, m=None, a=None, b=None):
        """Compute parameters and initial seed for LCG prng
        next_state = a*seed + b mod m

        Args:
            s(list): subsequent outputs from LCG oracle
            m(int/None)
            a(int/None)
            b(int/None)

        Returns:
            seed, a, b, m(int): assuming first state in s was derived from seed
        """
```