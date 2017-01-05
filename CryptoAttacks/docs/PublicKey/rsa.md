# RSA

```python
from CryptoAttacks.PublicKey import rsa

class RSAKey(Crypto.PublicKey.RSA._RSAobj):
    def __init__(self):
        """
        self.texts(list): list of dict [{'cipher': 12332, 'plain': 65432423}, {'cipher': 0xffaa, 'plain': 0xbb11}]
        self.identifier(string): id(self), filename or custom
        self.size(int): bit size
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

    def add_ciphertext(self, ciphertext):
        """Args: ciphertext(int)"""

    def add_plaintext(self, plaintext):
        """Args: plaintext(int)"""

    def add_text_pair(self, ciphertext=None, plaintext=None):
        """Args: ciphertext(int), plaintext(int)"""

    def clear_texts(self)

    def print_texts(self)

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


def small_e_msg(key, max_times=100):
    """If both e and plaintext are small, ciphertext may exceed modulus only a little

    Args:
        key(RSAKey): with small e, at least one ciphertext
        max_times(int): how many times plaintext**e exceeded modulus maximally

    Returns:
        dict: recovered plaintexts
        update key texts with found plaintexts
    """


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
                    every key with only one ciphertext

    Returns:
        bool/string: False on failure, recovered plaintext otherwise
        update keys texts
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
        dict: decrypted ciphertexts
        update key texts
    """


def signing_oracle(plaintext):
    """Function implementing parity oracle

    Args:
        plaintext(int)

    Returns:
        int: signature of given plaintext
    """
    raise NotImplementedError


def decryption_oracle(ciphertext):
    """Function implementing parity oracle

    Args:
        ciphertext(int)

    Returns:
        int: decrypted ciphertext
    """
    raise NotImplementedError


def blinding(key, signing_oracle=None, decryption_oracle=None):
    """Perform signature/ciphertext blinding attack

    Args:
        key(RSAKey): with at least one plaintext(to sign) or ciphertext(to decrypt)
        signing_oracle(function)
        decryption_oracle(function)

    Returns:
        dict: {index: signature/plaintext, index2: signature/plaintext}
        update key texts
    """


def bleichenbacher_signature_forgery(key, garbage='suffix', hash_function='sha1'):
    """Bleichenbacher's signature forgery based on bug in verify implementation

    Args:
        key(RSAKey): with small e and at least one plaintext
        garbage(string): middle: 00 01 ff garbage 00 ASN.1 HASH
                         suffix: 00 01 ff 00 ASN.1 HASH garbage
        hash_function(string)

    Returns:
        dict: forged signatures
        update key texts
    """


```