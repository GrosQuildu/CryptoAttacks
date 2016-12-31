# Cryptography attacks

### Requirements:
* Python 2.7
* [pycrypto](https://pypi.python.org/pypi/pycrypto)

### Attacks:
* Classic
	+ [One time pad / xor](#one-time-pad)
		+ Guess key size
		+ Repeated key
		+ Reused key
* Block
	+ [CBC](#cbc)
		+ Bit flipping
		+ Padding oracle
		* Key as IV
	+ [ECB](#ecb)
		+ Byte-at-time decryption
* Public Key
	+ [RSA](#rsa)
		+ Common primes
		+ Wiener's small private exponent
		+ Hastad's broadcast
		+ Faulty (RSA-CRT)
		+ Parity oracle

For example uses check tests

#### One time pad
```python
from CryptoAttacks.Classic import one_time_pad

def compare_by_frequencies(a, b, lang='English', no_of_comparisons=5):
    """Check which text have more similar letter frequencies (compared to language)
    todo: add words, diagraphs etc...

    Args:
        a(string)
        b(string)
        lang(string)
        no_of_comparisons(int): how much letters compare

    Returns:
        int: -1 if a is less similar than b, 0 if equal, 1 if a is more similar
    """

def break_one_char_key(ciphertext, lang='English', no_of_comparisons=5, alphabet=False, key_space=False,
                       reliability=100.0):
    """Brute for all one-char keys, return most language-like

    Args:
        ciphertext(string): text xored with short key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, plaintext)
    """

def guess_key_size(ciphertext, max_key_size=40):
    """Given sentence xored with short key, guess key size
    From: http://trustedsignal.blogspot.com/2015/06/xord-play-normalized-hamming-distance.html

    Args:
         ciphertext(string)
         max_key_size(int)

    Returns:
        list: sorted list of tuples (key_size, probability),
        note that most probable key size not necessary have the largest probability
    """

def break_repeated_key(ciphertext, lang='English', no_of_comparisons=5, key_size=None, max_key_size=40,
                       alphabet=None, key_space=None, reliability=100.0):
    """Short key encrypted with long plaintext

    Args:
        ciphertext(string): text xored with short key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        key_size(int/None)
        max_key_size(int/None)
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, plaintext)
    """

def break_reuse_key(ciphertexts, lang='English', no_of_comparisons=5, alphabet=None,
                    key_space=None, reliability=100.0):
    """Sentences xored with the same key

    Args:
        ciphertexts(list): texts xored with the same key
        lang(string): key in frequencies dict
        no_of_comparisons(int): used during comparing by frequencies
        alphabet(string/None): plaintext space
        key_space(string/None): key space
        reliability(float): between 0 and 100, used during comparing by frequencies

    Returns:
        list: sorted (by frequencies) list of tuples (key, list(plaintexts))
    """
```

#### CBC
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
    """Make ciphertext so it will decrypt to given plaintext
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

#### ECB
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

#### RSA
```python
from CryptoAttacks.PublicKey import rsa

class RSAKey(Crypto.PublicKey.RSA._RSAobj):
    def __init__(self):
        """
        self.texts: list of dict [{'cipher': 12332, 'plain': 65432423}, {'cipher': 0xffaa, 'plain': 0xbb11}]
        self.identifier: id(self), filename or custom
        """

    def encrypt(self, plaintext):
        """Raw encryption
        Args: plaintext(int)
        Returns: pow(plaintext,e,n)
        """

    def decrypt(self, ciphertext):
        """Raw decryption
        Args: ciphertext
        Returns: pow(ciphertext, d, n)
        """

    def generate(identifier=None, *args, **kwargs):
        """
        identifier(string/None): unique identifier of key
        bits(int): key size
        e(int): public exponent
        randfunc(function)
        progress_func(function)
        """

    def construct(n, e=0x10001, d=None, p=None, q=None, identifier=''):
        """Construct key from tuple

        Args:
            n(long): RSA modulus
            e(long): Public exponent
            d(long): Private exponent (d). If key is private, one of d,p or q must be given
            p(long): First factor of n
            q(long): Second factor of n
            identifier(string): unique identifier of key
        Returns:
            RSAKey
        """

    def import_key(filename, identifier=None, *args, **kwargs):
        """Import key from file

        Args:
            filename(string): use it as key's id
            identifier(string/None): unique identifier of key
        Returns:
            RSAKey
        """
        tmp_key = PyRSA.importKey(open(filename).read(), *args, **kwargs)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        if identifier:
            tmp_key.identifier = identifier
        else:
            tmp_key.identifier = filename
        return tmp_key


def common_primes(keys):
    """Find common prime in keys modules

    Args:
        keys(list):  RSAKeys

    Returns:
        list:  RSAKeys for which factorization of n was found
    """

def wiener(key):
    """Wiener small private exponent attack
     If d < (1/3)*(N**(1/4)), d can be effectively recovered using continuous fractions

     Args:
        key(RSAKey): public rsa key to break

    Returns:
        bool/RSAKey: False if didn't break key, private key otherwise
    """

def hastad(keys):
    """Hastad's broadcast attack (small public exponent)
    Given at least e keys with public exponent equals to e and ciphertexts of the same plaintext,
    plaintext can be efficiently recovered

    Args:
        keys(list): RSAKeys, all with same public exponent e, len(keys) >= e,
                    every key with at least one ciphertext

    Returns:
        bool/string: False on failure, recovered plaintext otherwise
    """

def faulty(key, padding=None):
    """Faulty attack against crt-rsa, Boneh-DeMillo-Lipton
    sp = padding(m)**(d % p-1) % p
    sq' = padding(m)**(d % q-1) % q <--any error during computation
    s' = crt(sp, sq') % n <-- broken signature
    s = crt(sp, sq) % n <-- correct signature
    p = gcd(s'**e - u(m), n)
    p = gcd(s - s', n)

    Args:
        key(RSAKey): with at least one broken signature (key.texts[no]['cipher']) and corresponding
                     plaintext (key.texts[no]['plain']), or valid and broken signature
        padding(None/function): function used before signing message

    Returns:
        bool/RSAKey: False on failure, recovered private key otherwise
    """

def parity_oracle(ciphertext):
    """Function implementing parity oracle

    Args:
        ciphertext(int)

    Returns:
        int: 0 (if decrypted ciphertext is even) or 1 (is odd)
    """
    raise NotImplementedError

def parity(parity_oracle, key):
    """Given oracle that returns LSB of decrypted ciphertext we can decrypt whole ciphertext
    parity_oracle function must be implemented

    Args:
        parity_oracle(function)
        key(RSAKey): contains ciphertexts to decrypt

    Returns:
        list:  decrypted ciphertexts
    """
```