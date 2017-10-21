# Elliptic Curve Digital Signature Algorithm

```python
def generate_keys(G):
    """Generate ECDSA keys

    Args:
        G(EllipticCurvePoint_finite_field): base point

    Returns:
        public key, private key
    """

def sign(message, d, G, hash_function=None):
    """Sign ECDSA

    Args:
        message(int/arg for hash_function)
        d(int): private key
        G(EllipticCurvePoint_finite_field): base point
        hash_function(NoneType/callable)

    Returns:
        r,s
    """
    
def verify(message, signature, G, Q, hash_function=None):
    """Verify ECDSA signature

    Args:
        message(int/arg for hash_function)
        signature(tuple of ints): r, s
        G(EllipticCurvePoint_finite_field): base point
        Q(EllipticCurvePoint_finite_field): public key
        hash_function(NoneType/callable)

    Returns:
        True/False
    """

def recover_d_biased_k(q, messages, signatures, l, hash_function=None):
    """Recover ECDSA private key from message/signature pairs, when k (emphemeral key) lsb are biased to 0

    Args:
        q(int): base point's order
        messages(list)
        signatures(list): [(r,s), (r,s)]
        l(int): amount of bits biased to 0 in k (lsb)
        hash_function(NoneType/callable)
        
    Returns:
        private key(int)
    """
```