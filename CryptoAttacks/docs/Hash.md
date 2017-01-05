# Hash

```python
def merkle_damgard(data, initial_state, compression_function):
    """Merkle-Damgard construction

    Args:
        data(string)
        initial_state(list of ints)
        compression_function(function)

    Returns:
        final state(string)
    """


def length_extension(hash, size, new_message, type='sha1'):
    """Length extension attack: given hash(secret) and len(secret),
    compute new_hash and old_padding so that hash(secret+old_padding+new_message) == new_hash

    Args:
        hash(string): hash of secret value
        size(int): length of secret (in bytes)
        new_message(string)
        type(string): sha1 or md4

    Returns:
        tuple: (new_hash, old_padding+new_message)
    """


def compression_function_sha1(chunk, state):
    """Sha1 compression function

    Args:
        chunk(string): len(chunk) == 64
        state(list of ints): len(state) == 5

    Returns:
        list of ints: compressed state
    """


def sha1(data, initial_state=[0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0], padding=None):
    """Compute SHA1

    Args:
        data(string)
        initial_state(list of ints)
        padding(string/None): if None, padding will be computed

    Returns:
        digest(string)
    """


def compression_function_md4(chunk, state):
    """MD4 compression function, taken from: https://gist.github.com/tristanwietsma/5937448

    Args:
        chunk(string): len(chunk) == 64
        state(list of ints): len(state) == 4

    Returns:
        list of ints: compressed state
    """


def md4(data, initial_state=[0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476], padding=None):
    """Compute MD4

    Args:
        data(string)
        initial_state(list of ints)
        padding(string/None): if None, padding will be computed

    Returns:
        digest(string)
    """
```
