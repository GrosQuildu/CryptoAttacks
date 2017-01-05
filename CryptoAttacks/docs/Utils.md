
```python
def b2h(a, size=0):
    """Encode bytes to hex string"""


def h2b(a):
    """Decode hex string to bytes"""


def h2i(a):
    """Decode hex string to int"""


def i2h(a, size=0):
    """Encode int as hex string"""


def b2i(number_bytes, endian='big'):
    """Unpack bytes into int

    Args:
        number_bytes(string)
        endian(string): big/little

    Returns:
        int
    """


def i2b(number, size=0, endian='big', signed=False):
    """Pack int to bytes

    Args:
        number(int)
        size(int): minimum size in bits, 0 if whatever it takes
        endian(string): big/little
        signed(bool): pack as two's complement if True (size must be given)

    Returns:
        string
    """

def xor(*args, **kwargs):
    """Xor given values

        args - strings to be xored
        expand - don't expand strings to size of the longest string if False
    Return xored strings
    """

def add_padding(data, block_size=16):
    """add PKCS#7 padding"""

def strip_padding(data, block_size=16):
    """strip PKCS#7 padding"""

def add_rsa_signature_padding(data, size=1024, hash_function='sha1'):
    """add PKCS#1 v1.5 sign padding"""

def add_md_padding(data, endian='big'):
    """Merkle-Damgard padding

    Args: data(string)
    Returns: data+padding(string)
    """

```