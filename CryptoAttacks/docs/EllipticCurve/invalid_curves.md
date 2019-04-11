# Invalid curves attack

```python
def invalid_curves(EC, oracle, verify, curves=generate_invalid_curves, bound=None, max_factor=65536, min_factor=16, max_attempts=5000):
    """Invalid curves attack
        When somebody computes your_point * secret_key without checking if your_point lies on the curve

        If you use generate_invalid_curves (default function) and the secret key is not found:
        save generated primes as list (they are printed), generate more curves,
         add them to the list and run this function with curves == the list

    Args:
        EC(EllipticCurve)
        oracle(function): like invalid_curves_oracle
        verify(function): like invalid_curves_verify
        curves(list/generator): list of tuples (Elliptic Curve, order, small_factors) (EC, int, dict)
                                or generator returning such tuples
                                Curves must differ only in b component
        bound(int/None): compute secret modulo bound, default bound == P
                            if there are not enough small factors on the curves,
                            secret will be computed modulo something smaller
        max_factor(int/None): all factors in small_factors will be <= max_factor
        min_factor(int/None): all factors in small_factors will be >= min_factor
        max_attempts(int): limit random point generation

    Returns
        tuple(int,int): secret key % bound_reached, bound_reached
    """
    
def generate_invalid_curves(P, A, B, max_factor, min_factor=16):
    """For curve EC == y^2 = x^3 + A*x + B find curves y^2 = x^3 + A*x + B2
        (differs only in B parameter), such that their orders have some small factors

    Args:
        P(int): EC filed
        A(int): EC param A
        B(int): EC param B
        max_factor(int): found curves must have order with
                            at least one factor such that: min_factor <= factor <= max_factor and factor power == 1
        min_factor(int):
    
    Returns:
        yields tuples: (EllipticCurve, EC order, small_factors)
    """

def invalid_curves_oracle(point):
    """Oracle for invalid curves attack
        Should return point * secret_key in some form,
        so the output can be verified.
        In simplest form it should return {'x':x, 'y':y) dict (== point * secret_key)
    
    Args:
        point(EC point)

    Returns:
        Whatever, it will be passed to invalid_curves_verify
    """

def invalid_curves_verify(K, *args):
    """Verifier for invalid curves attack
        It should check if K == some_func(*args)
        In simplest form it should check if K.x == args[0].x and K.y == args[0].y
    
    Args:
        K(EC point)
        args(output from invalid_curves_oracle)

    Returns:
        Bool
    """
```
