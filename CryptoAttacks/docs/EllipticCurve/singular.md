# Singular Curves

```python
def log_singular(f, p, P, Q):
    """Discrete logarithm on singular curve
    Q = d*P
    From: "Elliptic Curves: Number Theory and Cryptography, 2nd edition" by Washington (sec 2.10)

    Args:
        f(polynomial): curve equation (only x variable, may be over Rational Field)
            it is assumed that on left side of curve equation is y^2
        p(int): curve over finite field of size p
        P(tuple(int)): (x, y)
        Q(tuple(int)): (x, y)

    Returns:
        finite_rings.integer_mod: d
        tuple(finite_rings.integer_mod): (dx, dy)
    """

def log_cusp(P, Q):
    """Discrete logarithm on singular curve - cusp
    Assumption:
        Q = d*P
        y^2 = x^3
        singular point is (0,0)

    Args:
        P(tuple(finite_rings.integer_mod)): (x, y)
        Q(tuple(finite_rings.integer_mod)): (x, y)

    Returns:
        finite_rings.integer_mod: d
        tuple(finite_rings.integer_mod): (dx, dy)
    """

def log_node(p, P, Q, a):
    """Discrete logarithm on singular curve - node
    Assumptions:
        Q = d*P
        y^2 = x^2 * (x+a)
        singular point is (0,0)

    Args:
        p(int): curve over finite field of size p
        P(tuple(finite_rings.integer_mod)): (x, y)
        Q(tuple(finite_rings.integer_mod)): (x, y)
        a(int): root of curve equation

    Returns:
        finite_rings.integer_mod: d
        tuple(finite_rings.integer_mod): (dx, dy)
    """
```