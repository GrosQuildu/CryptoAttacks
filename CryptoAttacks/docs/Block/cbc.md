# CBC

```python
from CryptoAttacks.Block import cbc

def padding_oracle(payload, iv):
    """Function implementing padding oracle

    Args:
        payload(string): ciphertext to check
        iv(string): initialization vector (most often: append it at beginning of payload)

    Returns:
        bool: True if padding is correct, False otherwise
    """
    raise NotImplementedError

def decryption_oracle(payload, iv):
    """Function implementing decryption oracle. Have to work with ciphertexts that decrypt to
    incorrectly padded plaintexts, so before decryption you should append two blocks
    that will decrypt to something with valid padding, and return properly stripped plaintext

    Args:
        payload(string): ciphertext to decrypt
        iv(string): initialization vector (most often: append it at beginning of payload)

    Returns:
        string: decrypted ciphertext (don't strip with padding)
    """
    raise NotImplementedError

def decrypt(ciphertext, padding_oracle=None, decryption_oracle=None, iv=None, block_size=16,
            is_correct=True, amount=0, known_plaintext=None, async=False):
    """Decrypt ciphertext using padding oracle
    Give padding_oracle or decryption_oracle (or both)

    Args:
        ciphertext(string): to decrypt
        padding_oracle(function/None)
        decryption_oracle(function/None)
        iv(string): if not specified, first block of ciphertext is treated as iv
        block_size(int)
        is_correct(bool): set if ciphertext will decrypt to something with correct padding
        amount(int): how much blocks decrypt (counting from last), zero (default) means all
        known_plaintext(string): with padding, from end
        async(bool): make asynchronous calls to oracle (not implemented yet)

    Returns:
        plaintext(string): with padding
    """

def fake_ciphertext(new_plaintext, padding_oracle=None, decryption_oracle=None, original_ciphertext=None,
                    iv=None, original_plaintext=None, block_size=16):
    """Make ciphertext that will decrypt to given plaintext
    Give padding_oracle or decryption_oracle (or both)

    Args:
        new_plaintext(string): with padding
        padding_oracle(function/None)
        decryption_oracle(function/None)
        original_ciphertext(string): have to be correct,
                                    len(new_plaintext) == len(original_ciphertext)+len(iv)-len(block_size)
        iv(string): if not specified, first block of ciphertext is treated as iv
        original_plaintext(string): corresponding to original_ciphertext, with padding,
                                    only last len(block_size) bytes will be used
        block_size(int)

    Returns:
        fake_ciphertext(string): fake ciphertext that will decrypt to new_plaintext
    """

def bit_flipping(ciphertext, plaintext, wanted, block_size=16):
    """Given ciphertext and corresponding plaintext (two blocks) we can set first block of ciphertext
    so that last block of plaintext will be our wanted value

    Args:
        ciphertext(string): size == 2*block_size
        plaintext(string): size == block_size, plaintext of second ciphertext block
        wanted(string): size == block_size, we want ciphertext last block decrypt to this
        block_size(int)

    Returns:
        string: ciphertext that will decrypt to garbage_block+wanted_last_block
    """

def iv_as_key(padding_oracle=None, decryption_oracle=None, ciphertext=None, plaintext=None, block_size=16):
    """If iv is used as key, we can recover it using decryption (or padding) oracle
    Give padding_oracle or decryption_oracle or ciphertext and plaintext pair

    Args:
        padding_oracle(function/None)
        decryption_oracle(function/None)
        ciphertext(string/None): first block must be AES.encrypt(iv xor whatever),
                                 first block repeated at least once
        plaintext(string/None): with padding
        block_size(int)

    Returns
        string: key (==iv)
    """
```