# CBC

```python
from CryptoAttacks.Block import gcm


def recover_key_repated_nonce(ciphertexts_additionals_tags):
    """Recover authentication key for GCM given ciphertext encrypted with repeated nonce
    Sometimes fail (maybe bug in factorization)
    
    Args:
        ciphertexts_additionals_tags(list(tuple(bytes))): [(ciphertext, additional_data, auth_tag), ...]

    Returns:
        set(bytes): candidates for GCM auth key
    """

def deg(n):
    """Find degree of polynomial
    
    Args:
        n(Polynomial_128/list/int)
    
    Returns:
        int
    """

class Polynomial_2():
    """Polynomial with coefficients in GF(2)"""

    def __init__(self, coefficients):
        """x^3 + x + 1  == 0b1101 == [3, 1, 0]"""

class GF_2k():
    """GF(2^k) with elements represented as polynomials with coefficients in GF(2)"""

    def __init__(self, coefficients, k, modulus):
        """x^3 + x + 1  == 0b1101"""

class Polynomial_128():
    """Polynomial with coefficients in GF(2^128)"""

    def __init__(self, coefficients):
        """12*x^2 + x + 43 == [GF_2k(43,128,m), GF_2k(1,128,m), GF_2k(12,128,m)]"""
```