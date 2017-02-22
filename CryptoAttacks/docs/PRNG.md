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


def compute_params(s):
    """Compute parameters and initial seed for LCG prng

    Args:
        s(list): subsequent outputs from LCG oracle

    Returns:
        seed(int): assuming first state in s was derived from seed
        a, b, m(ints): a,b,m(ints): next_state = a*seed + b mod m
    """
```