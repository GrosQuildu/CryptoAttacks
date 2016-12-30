import itertools
from copy import deepcopy

from Crypto.PublicKey import RSA as PyRSA
from GrosCrypto.Math import *
from GrosCrypto.Utils import *


class RSAKey(PyRSA._RSAobj):
    def __init__(self):
        # log.critical_error("Create RSAKey via generate, construct or import_key method")
        self.texts = []  # list of dict [{'cipher': 12332, 'plain': 65432423}, {'cipher': 0xffaa, 'plain': 0xbb11}]
        self.identifier = ''

    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)

    def copy(self, identifier=''):
        if self.has_private():
            tmp = RSAKey.construct(self.n, self.e, self.d, self.p, self.q, identifier=identifier)
            tmp.texts = deepcopy(self.texts)
        else:
            tmp = RSAKey.construct(self.n, self.e, identifier=identifier)
            tmp.texts = deepcopy(self.texts)
        return tmp

    def publickey(self, identifier=''):
        tmp = RSAKey.construct(self.n, self.e, identifier=identifier)
        tmp.texts = deepcopy(self.texts)
        return tmp

    @staticmethod
    def generate(*args, **kwargs):
        tmp_key = PyRSA.generate(*args, **kwargs)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        tmp_key.identifier = id(tmp_key)
        return tmp_key

    @staticmethod
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
        if d or p or q:
            if not d:
                p = p or q
                d = long(gmpy2.invert(e, (p - 1)*(n/p - 1)))
            tup = (n, e, d)
        else:
            tup = (n, e)

        tmp_key = PyRSA.construct(tup)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        if identifier:
            tmp_key.identifier = identifier
        else:
            tmp_key.identifier = id(tmp_key)
        return tmp_key

    @staticmethod
    def import_key(filename, *args, **kwargs):
        """Import key from file

        Args:
            filename(string): use it as key's id
        Returns:
            RSAKey
        """
        tmp_key = PyRSA.importKey(open(filename).read(), *args, **kwargs)
        tmp_key.__class__ = RSAKey
        tmp_key.__init__()
        tmp_key.identifier = filename
        return tmp_key


def common_primes(keys):
    """Find common prime in keys modules

    Args:
        keys(list):  RSAKeys

    Returns:
        list:  RSAKeys for which factorization of n was found
    """
    priv_keys = []
    for pair in itertools.combinations(keys, 2):
        prime = gmpy2.gcd(pair[0].n, pair[1].n)
        if prime != 1:
            log.info("Found common prime in: {}, {}".format(pair[0].identifier, pair[1].identifier))
            for x in xrange(2):
                if pair[x] not in priv_keys:
                    d = long(gmpy2.invert(pair[x].e, (prime - 1) * (pair[x].n/prime - 1)))
                    priv_keys.append(RSAKey.construct(long(pair[x].n), long(pair[x].e), long(d), identifier=pair[x].identifier))
                else:
                    log.debug("Key {} already in priv_keys".format(pair[x].identifier))
    return priv_keys


def wiener(key):
    """Wiener small private exponent attack
     If d < (1/3)*(N**(1/4)), d can be effectively recovered using continuous fractions

     Args:
        key(RSAKey): public rsa key to break

    Returns:
        bool/RSAKey: False if didn't break key, private key otherwise
    """
    en_fractions = continued_fractions(key.e, key.n)
    for k, d in convergents(en_fractions):
        if k != 0 and (key.e * d - 1) % k == 0:
            phi = (key.e * d - 1) // k
            """ p**2 - p*(n - phi + 1) + n == 0 """
            b = key.n - phi + 1
            delta = b*b - 4*key.n
            if delta > 0:
                sqrt_delta = gmpy2.isqrt(delta)
                if sqrt_delta*sqrt_delta == delta and sqrt_delta % 2 == 0:
                    log.debug("Found private key (d={}) for {}".format(d, key.identifier))
                    key = RSAKey.construct(long(key.n), long(key.e), long(d), identifier=key.identifier)
                    return key
    return False


def hastad(keys):
    """Hastad's broadcast attack (small public exponent)
    Given at least e keys with public exponent equals to e and ciphertexts of the same plaintext,
    plaintext can be efficiently recovered

    Args:
        keys(list):  RSAKeys, all with same public exponent e, len(keys) >= e, all with at least one ciphertext

    Returns:
        bool/string: False on failure, recovered plaintext otherwise
    """
    e = keys[0].e
    if len(keys) < e:
        log.critical_error("Not enough keys, e={}".format(e))

    ciphertexts, modules = [], []
    for key in keys:
        if key.n not in modules and key.texts[0]['cipher'] not in ciphertexts:
            if key.e == e:
                modules.append(key.n)
                ciphertexts.append(key.texts[0]['cipher'])
            else:
                log.info("Key {} have different e(={})".format(key.identifier, key.e))

    if len(modules) < e:
        log.critical_error("Not enough keys with unique modulus and ciphertext, e={}, len(modules)=".format(e, len(modules)))
    if len(modules) > e:
        log.info("Number of modules/ciphertexts larger than e")

    result = crt(ciphertexts, modules)
    plaintext, correct = gmpy2.iroot(result, e)
    if correct:
        return long(plaintext)
    else:
        log.debug("Plaintext wasn't {}-th root")
        log.debug("result (from crt) = {}".format(e, result))
        log.debug("plaintext ({}-th root of result) = {}".format(e, plaintext))
        return False


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

    log.debug("Check signature-message pairs")
    for pair in key.texts:
        if 'plain' in pair and 'cipher' in pair:
            signature = gmpy2.mpz(pair['cipher'])
            message = pair['plain']
            if padding:
                message = padding(message)
            p = gmpy2.gcd(pow(signature, key.e) - message, key.n)
            if p != 1 and p != key.n:
                log.debug("Found p={}".format(p))
                key = RSAKey.construct(key.n, key.e, p=long(p))
                return key

    log.debug("Check for valid-invalid signatures")
    signatures = [tmp['cipher'] for tmp in key.texts if 'cipher' in tmp]
    for pair in itertools.combinations(signatures, 2):
        p = gmpy2.gcd(pair[0] - pair[1], key.n)
        if p != 1 and p != key.n:
            log.debug("Found p={}".format(p))
            key = RSAKey.construct(key.n, key.e, p=long(p))
            return key
    return False


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
    try:
        parity_oracle(1)
    except NotImplementedError:
        log.critical_error("Parity oracle not implemented")

    for cipher in [pair['cipher'] for pair in key.texts if 'plain' not in pair and 'cipher' in pair]:
        log.info("Decrypting {}".format(cipher))
        two_encrypted = key.encrypt(2)

        counter = lower_bound = numerator = 0
        upper_bound = key.n
        denominator = 1
        while lower_bound+1 < upper_bound:
            cipher = (two_encrypted * cipher) % key.n
            denominator *= 2
            numerator *= 2
            counter += 1

            is_odd = parity_oracle(cipher)
            if is_odd:  # plaintext > n/(2**counter)
                numerator += 1
            lower_bound = (key.n * numerator) / denominator
            upper_bound = (key.n * (numerator+1)) / denominator

            log.debug("{} {} [{}, {}]".format(counter, is_odd, long(lower_bound), long(upper_bound)))
            log.debug("{}/{}  -  {}/{}\n".format(numerator, denominator, numerator+1, denominator))
        log.success("Decrypted: {}".format(i2b(upper_bound)))
        return upper_bound
