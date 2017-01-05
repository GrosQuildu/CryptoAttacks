# ECB

```python
from CryptoAttacks.Block import ecb

def encryption_oracle(payload):
    """Function implementing encryption oracle with ecb mode

    Args:
        payload(string): raw data to encrypt

    Returns:
        string
    """
    raise NotImplementedError


def is_ecb(cipher, block_size=16):
    """Check if there are repeated blocks in ciphertext

    Args:
        cipher(string)
        block_size(int)

    Returns:
        bool: True if there are repeated blocks (so it's probably ECB mode)
    """


def find_block_size(encryption_oracle, constant=True):
    """Determine block size if ecb mode

    Args:
        encryption_oracle(function)
        constant(bool): True if prefix and suffix have constant length

    Returns:
        int
    """


def find_prefix_suffix_size(encryption_oracle, block_size=16):
    """Determine prefix and suffix sizes if ecb mode, sizes must be constant

    Args:
        encryption_oracle(function)
        block_size(int)

    Returns:
        tuple(int,int): prefix_size, suffix_size
    """


def decrypt(encryption_oracle, constant=True, block_size=16, prefix_size=None, secret_size=None,
            alphabet=None):
    """Given encryption oracle which produce ecb(prefix || our_input || secret), find secret

    Args:
        encryption_oracle(function)
        constant(bool): True if prefix have constant length (secret must have constant length)
        block_size(int/None)
        prefix_size(int/None)
        secret_size(int/None)
        alphabet(string): plaintext space

    Returns:
        secret(string)
    """
```

