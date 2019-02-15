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

def dsks(G, message, signature, Q, hash_function):
    """Duplicate-Signature Key Selection on ECDSA
    Create key pair and domain parameter G that verifies given signature

    So if we have someone's public key Q and signature (r,s) of some message signed
    with corresponding private key we can create new key pair that will verify
    the signature IF we also change base point G 


    Args:
        G(EllipticCurvePoint_finite_field): base point
        message(int/arg for hash_function)
        signature(tuple(int)): (r,s), signature of m
        Q(int): public key
        hash_function(NoneType/callable): converting message to int

    Returns:
        G'(EllipticCurvePoint_finite_field): new base point
        d'(int): new private key
        Q'(EllipticCurvePoint_finite_field): new public key, Q = d*G
    """
```